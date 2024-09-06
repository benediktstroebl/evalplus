
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    if not isinstance(text, str):
        return 'Variable that you passed as an argument is not a string'
    if text.isdigit():
        return 'Variable that you passed as an argument is not a string'
    if text.isalpha():
        return text.replace(' ', '_')
    if len(text) == 0:
        return 'Argument is empty'
    if ' ' not in text:
        return text
    else:
        if len(text.split()) == 1:
            return text.replace(' ', '_')
        else:
            text = text.replace(' ', '_')
            return text.replace('__', '-')

