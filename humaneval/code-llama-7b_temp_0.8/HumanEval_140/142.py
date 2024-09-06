
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
    text = text.strip()
    text_out = ''
    i = 0
    while i < len(text) - 1:
        if text[i] != ' ':
            text_out += text[i]
        else:
            j = i+1
            while j < len(text) and text[j] == ' ':
                j += 1
            text_out += '-' if (j-i) > 2 else '_'
            i = j-1
        i += 1
    text_out += text[-1] if text_out != '' else text
    return text_out
