
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
    text = text.strip()
    for i in range(0, len(text)):
        if text[i] == " ":
            if i < len(text)-1:
                if text[i+1] == " ":
                    if i < len(text)-2:
                        if text[i+2] == " ":
                            text = text[:i] + "-" + text[i+3:]
                            i += 3
                        else:
                            text = text[:i] + "-" + text[i+1:]
                            i += 1
                    else:
                        text = text[:i] + "-" + text[i+1:]
                        i += 1
                else:
                    text = text[:i] + "_" + text[i+1:]
                    i += 1
            else:
                text = text[:i] + "_" + text[i+1:]
                i += 1
    return text

