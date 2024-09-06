
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
    # todo:
    #   - use regex to replace the appropriate spaces
    #   - use .join() to join the string and replace the spaces with the "_"

    text = re.sub(r"\s+", "_", text)
    while "__" in text:
        text = re.sub("__", "_", text)

    return text


assert fix_spaces("Example") == "Example"
assert fix_spaces("Example 1") == "Example_1"
assert fix_spaces(" Example 2") == "_Example_2"
assert fix_spaces("Example   3") == "_Example-3"

