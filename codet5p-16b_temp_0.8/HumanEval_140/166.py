
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

    
    text_without_spaces = ""
    for c in text:
        if c!= " ":
            text_without_spaces += c
    
    text_without_spaces = text_without_spaces.replace(" ", "_")
    
    if text_without_spaces.count("  ") > 1:
        text_without_spaces = text_without_spaces.replace("  ", "-")
    
    return text_without_spaces
