
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
    new_text = []
    for i, char in enumerate(text):
        if char == " ":
            if i < len(text)-1 and text[i+1] == " ":
                new_text.append("_")
            else:
                new_text.append("-")
        else:
            new_text.append(char)
    return "".join(new_text)
