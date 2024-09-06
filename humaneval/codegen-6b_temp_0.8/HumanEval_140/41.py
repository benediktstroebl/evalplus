
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
    # remove everything except for spaces
    text = re.sub(r'[^\s]+','',text)
    # get rid of more than 2 consecutive spaces
    text = re.sub(r'\s\s+','_-',text)
    # add _ between consecutive spaces
    text = re.sub(r'\s+','_',text)
    return text
    