
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
        return text
    
    if " " not in text:
        return text
    
    text = re.sub(" ", "_", text)
    
    while text[0] == " ":
        text = text[1:]
    
    while text[-1] == " ":
        text = text[:-1]
        
    if text[0] == "_" and text[-1] == "_":
        return text[1:-1]
    else:
        return
