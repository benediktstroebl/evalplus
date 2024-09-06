
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
    text = text.split(' ')
    output = []
    for word in text:
        if word == "":
            output.append("_")
        elif len(word) > 2:
            output.append(word.replace(' ','-'))
        else:
            output.append(word.replace(' ','_'))
    return "".join(output)

