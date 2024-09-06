
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
    new_text = ""
    for index, char in enumerate(text):
        if index == len(text)-1:
            new_text+=char
        elif char == " " and text[index+1] == " ":
            new_text+=char
        else:
            new_text+=char
            
    return new_text
