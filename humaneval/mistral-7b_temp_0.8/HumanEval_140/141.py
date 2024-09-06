
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
    def fix_spaces_helper(text, i=0):
        if i >= len(text):
            return ''

        new_char = text[i]

        if new_char == ' ':
            if i > 0 and text[i-1] == ' ':
                return fix_spaces_helper(text, i + 1)
            else:
                return new_char + fix_spaces_helper(text, i + 1)
        else:
            return new_char + fix_spaces_helper(text, i + 1)

    return fix_spaces_helper(text)
