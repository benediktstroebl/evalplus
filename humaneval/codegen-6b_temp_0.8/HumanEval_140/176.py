
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
    if len(text) < 3:
        return text
    
    if not text[0].isalnum():
        return "_" + text
    
    ans = text[0]
    prev_char = None
    for char in text[1:]:
        if char.isalpha() and char != prev_char:
            ans += "_"
        ans += char
        prev_char = char
    
    return ans
        
        
    
    
