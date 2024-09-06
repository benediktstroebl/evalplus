
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
    if text == '':
        return text
    elif len(text) == 1:
        return text
    elif len(text) > 1:
        # list comprehension
        new_text = ''.join(['-' if text[i] == ' ' and text[i - 1] == ' ' else text[i] for i in range(len(text))])
        if len(new_text) == 1:
            return new_text
        else:
            return new_text.replace(' ', '_')
    else:
        return ''.join(['-' if text[i] == ' ' and text[i - 1] == ' ' else text[i] for i in range(len(text))])


