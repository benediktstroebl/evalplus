
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
    
    new_text = []
    i = 0
    space_count = 0
    while i < len(text):
        if text[i] == " ":
            if space_count == 1:
                new_text.append("-")
            space_count += 1
            new_text.append("_")
        elif space_count >= 2:
            new_text.append("-")
            space_count = 0
        else:
            new_text.append(text[i])
        
        i += 1
    return "".join(new_text)
