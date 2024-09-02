
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

    count = 0
    text = text.split(" ")
    for i in text:
        if len(i) > 2:
            count += len(i) - 2
            text[text.index(i)] = "_" + i[:2] + "-{}".format("_" * count)
            count = 0
    
    return "".join(text)
    
    
