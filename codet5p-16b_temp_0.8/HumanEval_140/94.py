
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

    
    text = text.replace(' ','_')
    output = ""
    count = 0
    for i in text:
        if i =='':
            count = count + 1
            output = output + '-'
        else:
            count = count - 1
            output = output + i
            
        if count == 0:
            output = output +''
            count = 0
            
    return output
            
            
            
            
    
    
