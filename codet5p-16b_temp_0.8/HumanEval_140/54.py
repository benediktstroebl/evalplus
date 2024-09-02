
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
        return ""
    
    fixed = []
    buffer = ""
    
    for char in text:
        if char == " ":
            fixed.append(buffer + "-")
            buffer = ""
            continue
        
        buffer += char
        
    if buffer == "":
        return text
    
    fixed.append(buffer)
    
    return "".join(fixed)
