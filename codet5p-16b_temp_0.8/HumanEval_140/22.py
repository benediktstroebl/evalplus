
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
    for char in text:
        if char == " ":
            count_spaces += 1
    
    if count_spaces <= 2:
        return text
    else:
        return_text = ""
        for i in range(len(text)):
            if text[i] == " ":
                return_text += "_"
            else:
                return_text += text[i]
        
        count_spaces = 0
        for char in return_text:
            if char == " ":
                count_spaces += 1
        
        if count_spaces > 2:
            return_text = ""
            for i in range(len(text)):
                if text[i] == " ":
                    return_text += "-"
                else:
                    return_text += text[i]
        return return_text
    
    
