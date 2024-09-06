
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
    words = text.split(' ')
    new_words = []
    for word in words:
        word = word.replace(" ", "_")
        if word!= " ":
            new_words.append(word)
    if len(new_words) == 1:
        return new_words[0]
    else:
        return "".join(new_words
