
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
    if text.find(' ') == -1:
        return text
    text_new = text.split()
    text_final = []
    for i in text_new:
        if len(text_new) > 1 and i == text_new[-1]:
            text_final.append(i)
        else:
            text_final.append(i.replace(' ','_'))
    return '-'.join(text_final)
