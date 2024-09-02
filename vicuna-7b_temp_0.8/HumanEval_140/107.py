
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
    def replace_consecutive(text):
        # replace multiple spaces with single space
        text = " ".join(text.split())
        # replace single space with -
        text = text.replace(" ", "-")
        # replace multiple spaces with -
        text = text.replace(" ", "-")
        return text
    return replace_consecutive(text)
