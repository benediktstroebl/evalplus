
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

    # replace spaces
    result = text.replace(" ", "_")

    # find 2+ spaces
    replace_spaces = " ".join(result.split(" ")[1::])

    # find consecutive spaces and replace with -
    result = replace_spaces.replace("  ", "-")

    # check if result is empty
    if len(result) == 0:
        return "_"
    else:
        return result
