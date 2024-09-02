
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

    
    new_text = []
    
    for i in range(len(text)):
        if text[i] =='':
            new_text.append('_')
        else:
            new_text.append(text[i])
            
    new_text = ''.join(new_text)
    
    while text[0] =='':
        new_text = new_text[1:]
        
        if len(new_text) == 0:
            return '_'
            
    if new_text[0] =='':
        new_text = new_text[1:]
        
    if new_text[-1] =='':
        new_text = new_text[:-1]
        
    if len(new_text) == 0:
        return '_'
        
    if new_text[-1] =='':
        new_text = new_text[:-1]
        
    if new_text[-1] =='':
        new_text = new_text[:-1]
        
