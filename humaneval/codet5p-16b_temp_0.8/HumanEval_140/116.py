
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

    
    spaces = []
    for i in range(len(text)):
        if text[i] == " ":
            spaces.append(i)
    if len(spaces) == 0:
        return text
    for i in range(len(spaces)-1):
        if spaces[i+1] - spaces[i] == 2:
            text = text[:spaces[i]] + '-' + text[spaces[i]+1:spaces[i+1]] + text[spaces[i+1]+1:]
    text = text.replace("  ", "-")
    return text

