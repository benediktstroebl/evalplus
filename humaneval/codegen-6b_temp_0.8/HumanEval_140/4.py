
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
    def replace_string(text, s1, s2):
        return text.replace(s1, s2)
    idx = None
    l = len(text)
    for i in range(l):
        if text[i] == " ":
            idx = i
            break
    if idx == None:
        return text
    if idx == 0:
        return replace_string(text, " ", "_")
    if idx == (l - 1):
        return replace_string(text, " ", "_")
    if text[idx - 1] != " ":
        return replace_string(text, " ", "_")
    return replace_string(text, " ", "-")
