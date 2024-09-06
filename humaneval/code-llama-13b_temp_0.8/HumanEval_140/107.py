
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
    if len(text) == 0:
        return text

    words = text.split(' ')
    new_text = words[0]

    for i in range(1, len(words)):
        if len(words[i]) > 0:
            if words[i][0].isalnum() and words[i - 1][-1].isalnum():
                new_text += '_'
            elif len(words[i - 1]) > 1 and words[i - 1][-1] == '_':
                new_text += '-'

        new_text += words[i]

    return new_text

