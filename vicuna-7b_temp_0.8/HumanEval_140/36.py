
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
        text = " ".join(text.split())
        text = "".join([word.lower() for word in text.split() if word.lower() not in "aeiou"])
        text = "_".join([word for word in text.split() if word.isalpha()])
        return text
    return replace_spaces(text)
