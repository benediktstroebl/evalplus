
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
    
    import re
    
    # Replace all spaces with underscores
    text = re.sub("\s", "_", text)

    # If text contains more than 2 consecutive spaces,
    # replace all consecutive spaces with -
    text = re.sub("\s{2,}", "-", text)
    
    return text
