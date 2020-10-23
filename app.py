import random
from flask import Flask, jsonify
from api.handlers import (
    get_tax_brackets
)
from api.error_handlers import format_error


app = Flask(__name__)


@app.errorhandler(404)
def not_found_handler(e):
    return jsonify({
        'errors': format_error(
            'That url was not found',
            code='NOT_FOUND'
        )
    }), 404

@app.errorhandler(Exception)
def exception_handler(e):
    return jsonify({
        'errors': format_error(str(e), code='INTERNAL_SERVER_ERROR')
    }), 500


@app.route('/')
def instructions():
    return 'instructions tbd'


@app.route('/tax-brackets')
def default_brackets():
    try:
        resp_dict = get_tax_brackets()
    except Exception as e:
        return jsonify({'errors': format_error(str(e))}), 400

    return jsonify(resp_dict)


@app.route('/tax-brackets/<tax_year>')
def tax_year_brackets(tax_year):

    # be evil
    # import pdb; pdb.set_trace()
    roulette = random.randint(1, 3)
    print(f'Roulette {roulette} (3 is bad today)')
    if roulette == 3:
        raise Exception("Database not found!")

    tax_brackets = get_tax_brackets(tax_year)

    return jsonify(tax_brackets)