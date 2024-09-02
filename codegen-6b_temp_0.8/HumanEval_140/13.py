
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
    intervals_of_spaces = [m for m in _SPACES_REGEX.finditer(text)]
    modified = text
    prev_space_end = 0
    for space_start, space_end in intervals_of_spaces:
        modified = "%s%s%s" % (modified[:prev_space_end], modified[prev_space_end:space_start], modified[space_end:])
        prev_space_end = space_end
    if modified[-1] ==" ":
        modified = modified[:-1]
    return modified.replace(" ", "_")
    