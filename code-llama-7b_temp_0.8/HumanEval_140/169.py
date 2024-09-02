
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

    # Traditional approach
    # new_text = ''
    # for i, letter in enumerate(text):
    #     if letter == ' ':
    #         if text[i-1] != ' ':
    #             new_text += '_'
    #         elif text[i-1] == ' ':
    #             new_text += '-'
    #     else:
    #         new_text += letter
    # return new_text
    
    # List comprehension approach
    return '_'.join(['-' if letter == ' ' * 3 else '_' if letter == ' ' else letter for letter in text])

