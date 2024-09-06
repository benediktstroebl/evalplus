
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
    if text == "":
        return text
    else:
        count = 0
        temp = ""
        for i in text:
            if i == " ":
                count += 1
            else:
                if count == 1:
                    temp += "_"
                    count = 0
                else:
                    if count >= 2:
                        temp += "-"
                    temp += i
        return temp

