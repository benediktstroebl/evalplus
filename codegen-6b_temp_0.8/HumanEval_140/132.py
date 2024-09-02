
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
    # replace
    text = text.replace(" ", "_")
    # strip
    text = text.strip("_")
    # Convert first letter into upper case
    if text[0].isalpha():
        text = text[0].upper() + text[1:]
    # replace consecutive spaces with -
    return "".join(["-", text[i].replace(" ", "-") if i < len(text) -1 and text[i] == " " and text[i+1] == " " else text[i] for i in range(len(text))])
