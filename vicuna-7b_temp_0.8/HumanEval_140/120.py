
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
    def replace_spaces(text):
        # Replace single spaces with underscores
        text = text.replace(" ", "_")
        # Replace consecutive spaces with - 
        # Note that we use a list comprehension and a regular expression
        # to make this more efficient than a loop
        return "_" + "".join([text.replace(" ", "") for _ in range(2)])
    return replace_spaces(text)
