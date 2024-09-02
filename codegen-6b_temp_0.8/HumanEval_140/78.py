
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
    if text == "":
        return ""
    
    # Remove spaces and convert to an array
    new_list = text.split(" ")
    
    # Remove all empty elements from the list
    while "" in new_list:
        new_list.remove("")
    
    # Split the list into a string
    new_string = " ".join(new_list)
    
    # Replace all spaces with underscores, then replace all consecutive spaces with -
    new_string = new_string.replace(" ", "_")
    new_string = new_string.replace("  ", " ")
    
    return new_string
