
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

    
    count_spaces = 0
    text_replaced = ""
    
    for i in range(len(text)):
        if text[i] == " ":
            count_spaces += 1
            if count_spaces < 2:
                text_replaced += "_"
            else:
                text_replaced += "-"
            
        else:
            text_replaced += text[i]
            count_spaces = 0
    
    return text_replaced

