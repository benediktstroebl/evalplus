
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
    
    text = text.replace(" ", "_")
    
    def remove_spces(text, offset):
        """
        Remove all spaces and also remove consecutive spaces, 
        and return the resulting string
        
        remove_spces("Example", 0) == "Example"
        remove_spces(" Example ", 4) == "Example"
        remove_spces("Example ", 2) == "Example"
        remove_spces(" Example   ", 6) == "Example"
        """
        text = text[:offset] + text[offset + 1:]
        
        while "  " in text:
            text = text.replace("  ", " ")
        
        return text
    
    # remove spaces from the left
    offset = 0
    while "  " in text[offset:]:
        offset += 1
    text = remove_spces(text, offset)
    
    # remove spaces from the right
    while text.endswith("_"):
        text = text[:-1]
    
    return text
