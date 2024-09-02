
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
    words = text.split()
    count = 0
    for i in range(len(words)):
        if count < 2:
            words[i] = words[i].replace(" ", "_")
            count += 1
        else:
            words[i] = words[i].replace(" ", "-")
            count = 0
    return "".join(words)
