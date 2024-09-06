
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

    
    count = 0
    while count < len(text)-1:
        if text[count] =='' and text[count+1] =='':
            text = text[:count] + '_' + text[count+2:]
            count -= 1
        count += 1
    return text
    
