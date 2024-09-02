
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

    if len(text) == 0:
        return ""
    curr_index = 0
    while curr_index < len(text):
        if text[curr_index] == " ":
            text = text[:curr_index] + "_" + text[curr_index+1:]
            if curr_index+2 < len(text):
                if text[curr_index+2] == " ":
                    text = text[:curr_index+2] + "_" + text[curr_index+3:]
                    if curr_index+4 < len(text):
                        if text[curr_index+4] == " ":
                            text = text[:curr_index+4] + "_" + text[curr_index+5:]
        curr_index += 1
    return text
