
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
    # initialize variables
    text = text.strip()
    spaces = 0
    spaces_count = 0
    results = []

    # loop through each character
    for char in text:
        if char.isspace():
            spaces += 1
            if spaces == 1:
                results.append(char)
            elif spaces == 2:
                results.append( "-" + char )
                spaces_count = 0
                spaces = 0
            else:
                spaces_count += 1
        else:
            spaces = 0
            results.append(char)

    # add the last group of 2 or more consecutive spaces
    if spaces > 0:
        results.append( "-" * (spaces * (2 - spaces_count)) )
    
    return "".join(results)
