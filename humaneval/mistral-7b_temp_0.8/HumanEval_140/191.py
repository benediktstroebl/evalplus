
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

    # your code here
    string_to_replace = " "
    text = text.replace(string_to_replace, "_")

    list_text = list(text)
    if len(list_text) < 3:
        return text
    else:
        count = 0
        for i in range(len(list_text)-2):
            if list_text[i] == " " and list_text[i + 1] == " " and list_text[i + 2] == " ":
                list_text[i] = "-"
                count += 1
        if count > 0:
            return "".join(list_text)
        else:
            return text

