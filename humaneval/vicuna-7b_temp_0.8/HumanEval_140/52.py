
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
    # Use a regular expression to replace multiple spaces with a single -
    text = re.sub(r'[ \t]+', '_', text)
    # Replace a single space with an underscore
    text = text.replace(' ', '_')
    return text
