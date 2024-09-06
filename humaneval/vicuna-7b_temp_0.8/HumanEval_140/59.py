
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
        # replace all consecutive spaces with -
        text = "_".join(text.split(" "))
        return text
        
    def replace_one(text):
        # replace all spaces with underscores
        text = "_".join(text.split(" "))
        return text
        
    def replace(text):
        if len(text.split(" ")) < 2:
            return text
        else:
            return replace_consecutive(replace_one(text))
        
    return replace(text)
