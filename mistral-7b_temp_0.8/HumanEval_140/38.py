
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
    text = text.replace(' ','_')
    #if there is more than two spaces, replace all with -
    text = text.replace('  ','-')
    return text
    
    #Here's the solution:
    # text = text.replace(' ','_')
    # text = text.replace('  ','-')
    # return text

    #Another solution:
    # text = ' '.join(text.split())
    # text = text.replace('  ','-')
    # return text

