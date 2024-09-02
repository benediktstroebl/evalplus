
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

    if len(text) <= 2:
        return text
    cnt = 0
    for i in range(1,len(text)):
        if text[i-1] == " " and text[i] == " ":
            cnt += 1
            if cnt > 2:
                return text[:i-1]+"-"+text[i+1:]
        else:
            cnt = 0
    return text
