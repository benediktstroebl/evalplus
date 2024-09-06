
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

    fixed_spaces = []
    for index, word in enumerate(text):
        if word == " ":
            fixed_spaces.append("_")
        elif index > 0:
            if text[index - 1] == " " and text[index] == " ":
                fixed_spaces.append("-")
            else:
                fixed_spaces.append(word)
        else:
            fixed_spaces.append(word)
    fixed_spaces = "".join(fixed_spaces)
    return fixed_spaces
    
