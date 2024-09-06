
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

    spaces_count = 0
    result = ""
    for c in text:
        if c == " ":
            spaces_count += 1
        else:
            result += "_" if spaces_count > 2 else "-".join(["_"] * spaces_count)
            spaces_count = 0
    return result

