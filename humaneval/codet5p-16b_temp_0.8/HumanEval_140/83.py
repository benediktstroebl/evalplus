
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

    
    temp = ""
    for i in text:
        if i == " ":
            temp += "_"
        else:
            temp += i
    
    result = ""
    for i in range(len(temp)):
        if temp[i] == "_" and i == 0:
            result += "_"
            continue
        if temp[i] == "_" and temp[i - 1]!= " ":
            result += "-"
        else:
            result += temp[i]
    
    return result

