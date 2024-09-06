
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
    # first, replace the spaces with underscores
    fixed_text = text.replace(" ", "_")

    # second, if the string has more than 2 consecutive spaces,
    # replace them with a _
    if fixed_text.count("_") > 2:
        fixed_text = re.sub(r'\s\s*','_',fixed_text)
    return fixed_text
