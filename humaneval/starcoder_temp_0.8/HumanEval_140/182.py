
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
    if text == "":
        return text
    if text.count(" ") == 0:
        return text
    elif text.count(" ") > 1:
        text_list = text.split()
        result = []
        for s in text_list:
            result.append(fix_spaces(s))
        return "_".join(result)
    else:
        return text.replace(" ", "_")
