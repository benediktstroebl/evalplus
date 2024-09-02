
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

    
    if len(text) < 3:
        return text
    
    counter = 1
    result = ""
    
    for i in range(len(text)-1):
        if text[i] == " ":
            if text[i+1] == " ":
                counter += 1
                if counter > 2:
                    result += "-";
                else:
                    result += "_"
            else:
                result += "_"
        else:
            result += text[i]
            
    return result + text[-1]



