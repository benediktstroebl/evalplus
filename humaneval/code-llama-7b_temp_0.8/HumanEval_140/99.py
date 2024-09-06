
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
    if not text or len(text) == 0:
        return text
    # split by space and strip whitespaces from both sides of the string
    # join by - if there are more than 2 consecutive spaces
    return "".join(map(lambda word: word if word == "" else "-" if len(word) > 2 else "_" + word + "_", text.split()))

