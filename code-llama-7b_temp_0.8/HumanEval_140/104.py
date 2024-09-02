
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
    # Your code here
    # initiate empty string to return
    result = ""
    
    # iterate through the string
    for i in text:
        # check for space
        if i == ' ':
            # check for more than two consecutive spaces
            if len(result[-1]) == 2:
                result += '-'
            else:
                result += '_'
        else:
            # if space is not found
            result += i
    
    return result
