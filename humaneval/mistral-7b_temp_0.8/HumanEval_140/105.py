
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
    words = text.split()
    fixed_words = []
    for word in words:
        if word == "":
            fixed_words.append("")
        elif word.count(" ") > 2:
            fixed_words.append("-".join(word.split()))
        else:
            fixed_words.append(word.replace(" ", "_"))
    return " ".join(fixed_words)

