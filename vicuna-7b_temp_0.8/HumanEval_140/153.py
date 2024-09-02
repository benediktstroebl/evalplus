
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
    # Initialize an empty list
    result = []
    
    # Use a regular expression to find all sequences of consecutive
    # spaces and replace them with a dash
    for match in re.finditer(r'\s+', text):
        result.append(text[match.start(): match.start() + len(match.group())])
    
    # Use a regular expression to find all individual spaces and replace them
    # with an underscore
    for match in re.finditer(r'\s', text):
        result.append(text[match.start(): match.start() + len(match.group())])
        
    return ' '.join(result)
