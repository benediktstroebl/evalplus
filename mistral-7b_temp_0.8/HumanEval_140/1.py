
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
    # for start_pos in range(len(text)):
    #     if text[start_pos] == ' ':
    #         if start_pos == 0:
    #             text = text[start_pos:]
    #             text = text.replace(' ', '_')
    #         elif start_pos == len(text)-1:
    #             text = text[:start_pos]
    #             text = text.replace(' ', '_')
    #         else:
    #             text = text[:start_pos]+text[start_pos+1:]
    #             text = text.replace(' ', '_')
    #         text = text.replace('  ', '-')
    #         return text
    # return text
    return text.replace(' ', '_').replace('  ', '-')

