
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

    
    space_indices = []
    
    for i in range(len(text)):
        if text[i] =='':
            space_indices.append(i)
            
    if len(space_indices) > 2:
        new_text = text[0]
        
        for i in range(len(space_indices)):
            if i == 0:
                new_text += "_"
            elif i == len(space_indices) - 1:
                new_text += "_"
            else:
                new_text += "-"
            
            if i < len(space_indices) - 1:
                new_text += text[space_indices[i] + 1:space_indices[i + 1]]
                
        return new_text
    else:
        return text
        
