
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
    if text.strip() == '':
        return ''
    
    list_text = list(text)
    len_text = len(list_text)
    
    start = 0
    while start < len_text:
        while list_text[start] == ' ':
            start += 1
            
        if start == len_text - 1:
            list_text[start] = '_'
            break
        
        i = start
        while list_text[i] != ' ':
            i += 1
            if i == len_text - 1:
                break
            
        if list_text[i] == ' ':
            if list_text[i - 1] == ' ':
                list_text[i] = '-'
            else:
                list_text[i] = '_'
        else:
            i -= 1
            if list_text[i] == ' ':
                list_text[i] = '_'
        
        start = i + 1
    
    return ''.join(list_text)

