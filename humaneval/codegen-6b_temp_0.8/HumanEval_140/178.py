
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
    # Please write your code below
    i = 0
    j = 0
    l = len(text)
    while True:
        while j < l and text[j] == ' ':
            j += 1
        if j == l:
            return text
        if j < l and text[j] != ' ':
            text = text[:i] + "_" + text[j:]
            i = j + 1
            j = 0
        else:
            j += 1
    return text
