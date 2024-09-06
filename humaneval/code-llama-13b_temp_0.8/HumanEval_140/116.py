
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
    # if text is empty return None
    if text == '':
        return None
    # change spaces to _
    new_text = text.replace(' ', '_')
    # add _ in the begining if first letter is not _
    if new_text[0] != '_':
        new_text = '_' + new_text
    # add _ in the end if last letter is not _
    if new_text[-1] != '_':
        new_text = new_text + '_'
    # replace spaces with -
    new_text = new_text.replace('  ', '-')
    return new_text
