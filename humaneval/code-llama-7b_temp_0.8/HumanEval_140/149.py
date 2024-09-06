
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
    temp = text.split()
    for i in range(len(temp)):
        if i % 2 == 0:
            temp[i] = temp[i].replace(" ","_")
        else:
            temp[i] = temp[i].replace(" ","-")
    temp = "".join(temp)
    return temp
