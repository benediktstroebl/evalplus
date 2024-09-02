
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
    # replace single spaces with underscores
    text = text.replace(' ', '_')
    
    # replace consecutive spaces with -
    # using a list to store the location of consecutive spaces
    space_locations = [0]
    for char in text:
        if char == ' ':
            space_locations.append(space_locations[-1] + 1)
        elif char.isspace():
            space_locations[-1] += 1
    
    # replace consecutive spaces with -
    return '-' + '-'.join(['_' for i in space_locations[:-1]])
