
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
    
    def _fix_spaces(text):
        if len(text) < 3:
            return text
        
        text = re.sub(" +", " ", text)
        if " " in text[1:-1]:
            text = text[0] + "-" + text[-1]
        return text[0] + re.sub(" ", "_", text[1:-1]) + text[-1]
    
    while True:
        new_text = _fix_spaces(text)
        if new_text == text:
            return new_text
        text = new_text
