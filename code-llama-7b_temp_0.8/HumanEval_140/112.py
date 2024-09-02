
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
    # new_text = text.replace(" ", "_")
    new_text = text
    for i in range(len(new_text)-2):
        if new_text[i] == " " and new_text[i+1] == " ":
            new_text = new_text[:i] + "-" + new_text[i:]
    return new_text.replace(" ", "_")
