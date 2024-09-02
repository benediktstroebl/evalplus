
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
    result = ""
    for word in text.split(" "):
        if word == "":
            continue
        if len(word) > 3:
            word = "_" * (len(word) - 3) + word[-3:]
        result += word + " "
    return result[:-1]

