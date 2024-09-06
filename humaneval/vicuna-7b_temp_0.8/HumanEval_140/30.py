
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
    # Split the string into a list of words
    words = text.split()
    # Create an empty string to store the fixed text
    fixed_text = ""
    # Loop through the words and replace spaces with underscores
    for i, word in enumerate(words):
        # If the word has only one space, add it to the fixed text
        if word.count(" ") == 1:
            fixed_text += "_" + word
        # If the word has two or more consecutive spaces, replace all consecutive spaces with -
        elif word.count(" ") > 1:
            fixed_text += "_" + word.replace(" ", "-")
        # Otherwise, add the word to the fixed text as-is
        else:
            fixed_text += word
    return fixed_text
