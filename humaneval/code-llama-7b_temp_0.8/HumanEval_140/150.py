
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
    
    text_list = list(text)
    i = 0
    while i < len(text_list):
        if text_list[i] == " ":
            while text_list[i] == " ":
                if i > len(text_list) - 2:
                    break
                else:
                    text_list[i] = "_"
                    i += 1
            if text_list[i] == " ":
                while text_list[i] == " ":
                    text_list[i] = "-"
                    i += 1
            else:
                i += 1
        else:
            i += 1

    text_list = [i for i in text_list if i != "_"]
    text = "".join(text_list)
    return text

