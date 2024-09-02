

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper() + string[1:]
    return string.lower()

@app.callback(
    Output('trade_grid', 'children'),
    [Input('symbol_dropdown', 'value')],
    [Input('flip_case', 'value')]
)
