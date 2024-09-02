
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

    # replacing spaces with underscores
    text = text.replace(' ', '_')
    # get the amount of times spaces occur
    amount = text.count('_')
    # if the amount of spaces is greater than 2 then replace with -
    if amount > 2:
        text = text.replace('_', '-')
    return text


