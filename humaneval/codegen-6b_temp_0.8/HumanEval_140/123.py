
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
    
    if not text:
        return ""
    
    fixed = text[0]
    for char in text[1:]:
        if char == " ":
            fixed += "_"
        else:
            fixed += char
    
    bulleted_spaces = re.findall("\s{2,}", fixed)
    for space in bulleted_spaces:
        fixed = fixed.replace(space, "")
        fixed += "-"
    return fixed


