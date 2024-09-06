
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
    
    if text.count(" ")==0: return text
    if text.count(" ")==1: return text.replace(" ", "_") 
    if text.count(" ")==2: return text.replace(" ", "-")
    
    replace = 0
    for i in range(0,len(text)):
        if text[i]==" ":
            replace+=1
        elif replace>0: 
            text = text[0:i] + "_" + text[i+1:]
            replace-=1
    return text
