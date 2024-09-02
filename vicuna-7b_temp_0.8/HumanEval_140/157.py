
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
    # split text into words
    words = text.split()
    
    # replace consecutive spaces with -
    result = []
    last_word = ""
    for word in words:
        if len(word) > 2:
            if word.startswith(" "):
                result.append(word.lstrip(" "))
            else:
                result.append(word)
        else:
            if last_word.endswith(" "):
                result.append(last_word.rstrip(" "))
            else:
                result.append(last_word + word)
            last_word = word.strip()
    return " ".join(result)