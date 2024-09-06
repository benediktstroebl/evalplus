
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
        result = ""
        n = 0
        for char in text:
            if char == " ":
                result += "_"
                n += 1
            else:
                result += char
                n = 0
        return result + "_" * (2 - n)
    
    return replace_spaces(text)
