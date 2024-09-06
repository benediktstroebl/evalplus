
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
    # 1. use regex to match space and replace with underscore
    # 2. use regex to match more than two consecutive spaces and replace with -
    return re.sub(r"( )+", r"_", re.sub(r"\s{2,}", r"-", text))
    # return re.sub(r"\s{2,}", r"-", re.sub(r"( )+", r"_", text))
