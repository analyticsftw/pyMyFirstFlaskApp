from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    html = '<h1>Temperature converter</h1>'
    html += '''
        <form action="/solution" method="post">
            <p>
            Enter a value: <br/>
            <input name="value_from" value="32" />
            </p>
            <p>Converting from:
            <fieldset>
                <input type="radio" name="unit_from" id="from_celcius" value="c" checked/>
                <label for="from_celcius">Celcius (C)</label>
                
                <input type="radio" name="unit_from" id="from_fahrenheit" value="f"/>
                <label for="from_fahrenheit">Fahrenheit (F)</label>

                <input type="radio" name="unit_from" id="from_kelvin" value="k"/>               
                <label for="from_kelvin">Kelvin (K)</label>
            </fieldset>
            </p>
            <p>Converting to:
            <fieldset>
                <input type="radio" name="unit_to" id="to_celcius" value="c"/>
                <label for="to_celcius">Celcius (C)</label>
                
                <input type="radio" name="unit_to" id="to_fahrenheit" value="f" checked/>
                <label for="to_fahrenheit">Fahrenheit (F)</label>
                
                <input type="radio" name="unit_to" id="to_kelvin" value="k"/>
                <label for="to_kelvin">Kelvin (K)</label>
            </fieldset>
            </p>
            <input type="submit"/>
        </form>'''
    return html

@app.route('/solution', methods=('GET', 'POST'))
def solution():
    conv_value = float(0)
    args  = request.form.to_dict(flat=True)

    conv_value = float(args['value_from']) if args['value_from'] else 0
    conv_unit_from = args['unit_from']
    conv_unit_to = args['unit_to']

    if conv_unit_from == "c":
        if conv_unit_to == "c":
            new_value = conv_value
        if conv_unit_to == "f":
            new_value = (conv_value * 1.8) + 32
        if conv_unit_to == "k":
            new_value = conv_value + 273.15
    if conv_unit_from == "f":
        if conv_unit_to == "c":
            new_value = (conv_value - 32) / 1.8
        if conv_unit_to == "f":
            new_value = conv_value
        if conv_unit_to == "k":
            new_value =  (conv_value - 32) / 1.8 + 273.15
    if conv_unit_from == "k":
        if conv_unit_to == "c":
            new_value = (conv_value - 273.15)
        if conv_unit_to == "f":
            new_value =  (conv_value - 273.15) * 1.8 +32
        if conv_unit_to == "k":
            new_value =  conv_value
    conv_msg = " (duh)" if conv_unit_from == conv_unit_to else ""
    html = '<h1>We\'ve got your solution</h1>'
    html += '<p><strong>{}&deg;{}</strong> is equal to <strong>{}&deg;{}</strong>{}.</p>'.format(conv_value, conv_unit_from.capitalize(), '{:.2f}'.format(new_value), conv_unit_to.capitalize(), conv_msg)
    html += '<hr><a href="/">Try again?</a>'
    return html