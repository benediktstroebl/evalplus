
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
    for char in text:
        if char == " ":
            if not new_text or new_text[-1]!= "_":
                new_text.append("_")
        else:
            new_text.append(char)
    return "".join(new_text)

