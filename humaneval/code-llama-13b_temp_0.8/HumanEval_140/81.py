
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
    # if not text:
    #     return text
    # text = text.replace(' ', '_')
    # return text.replace('  ', '-')
    if not text:
        return text
    new_text = []
    text = text.split()
    for word in text:
        new_text.append(word.replace(' ', '_'))
    return '-'.join(new_text)
    # print(text)
    # for i, word in enumerate(text):
    #     # new_text += word.replace(' ', '_')
    #     new_text[i] = word.replace(' ', '_')
    # # return ''.join(new_text)
    # return new_text.replace('  ', '-')
    # return ''.join(new_text).replace('  ', '-')


