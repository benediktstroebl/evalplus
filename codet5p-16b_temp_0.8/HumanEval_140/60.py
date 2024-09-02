
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

    
    if len(text) < 2: # If a string has less than 2 characters, return it as is
        return text
    
    new_text = "" # The new string
    i = 0 # The index of the string
    while i < len(text): # While we are within the string
        if text[i]!= " ":
            new_text += text[i] # Add the character to the string
        else:
            if i+1 < len(text): # If we are on the second or later character, add the underscore
                new_text += "_"
            else:
                new_text += "-" # If we are on the second to last character, add a dash
        i += 1
    return new_text
