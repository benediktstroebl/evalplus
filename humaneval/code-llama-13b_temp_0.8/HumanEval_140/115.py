
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
    # if len(text) == 0:
    #     return text
    
    # text = text.replace(' ', '_')
    
    # index = 0
    # while index < len(text):
    #     if text[index] == '_' and index < len(text) - 1:
    #         if text[index+1] == '_':
    #             text = text[:index] + '-' + text[index+1:]
    #     index += 1
    # return text
    
    # optimized solution
    return text.replace(' ', '_').replace('__', '-')
