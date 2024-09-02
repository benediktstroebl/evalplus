
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
    if not text:
        return text
    
    output = ''
    current_char = text[0]
    current_char_count = 0
    for i in range(1, len(text)):
        if text[i] == ' ':
            if current_char_count >= 2:
                output += '-'
            else:
                output += '_'
            current_char_count = 0
            current_char = text[i]
        else:
            if current_char != text[i]:
                if current_char_count >= 2:
                    output += '-'
                else:
                    output += '_'
                current_char_count = 0
                current_char = text[i]
            current_char_count += 1
            output += current_char
    return output

