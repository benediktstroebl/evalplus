
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
    if text == "":
        return ""
    if text.find(" ") == -1:
        return text
    text_list = text.split(" ")
    new_text = ""
    for word in text_list:
        if word.find(" ") == -1:
            new_text += word
        else:
            if word.find(" ") == 0 or word.find(" ") == -2:
                new_text += word
            else:
                new_text += "_"
    if new_text.find("__") != -1:
        for i in range(0, len(new_text), 2):
            if new_text[i:i+2] == "__":
                new_text = new_text[:i] + "-" + new_text[i+2:]
    return new_text
