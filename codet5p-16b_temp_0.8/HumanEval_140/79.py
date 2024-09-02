
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

    new_string = ""
    for ch in text:
        if ch == " ":
            new_string += "_"
        else:
            new_string += ch
    
    out = ""
    in_word = False
    for ch in new_string:
        if ch == "_":
            in_word = True
            continue
        elif ch == "-":
            in_word = False
            continue
        else:
            if in_word:
                continue
            else:
                out += ch
    return out

