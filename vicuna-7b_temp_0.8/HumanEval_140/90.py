
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
    # define a regular expression to match a sequence of consecutive spaces
    space_regex = r'\s+', re.compile(r'\s+')

    # use string methods to replace all occurrences of the regular expression
    # with either an underscore or a hyphen, followed by a 3-digit number
    return space_regex.sub('_%d_', text)
