
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
    count = 0
    
    for index, i in enumerate(text):
        if i == " ":
            count += 1
            if count > 2:
                new_text.append("-")
            else:
                new_text.append("_")
        else:
            count = 0
            new_text.append(i)
    
    return "".join(new_text)
