
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
    # space = r"\s+"
    # replace_string = r"_"
    # dash = r"-"

    if len(text) == 0 or type(text) != str:
        return False
    else:
        text_new = re.sub(r"\s+", "_", text)
        if "__" in text_new:
            text_new = text_new.replace("__", "-")

    return text_new
