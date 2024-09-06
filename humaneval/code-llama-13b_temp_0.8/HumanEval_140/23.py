
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
    if text.count("  ") == 0:
        text = text.replace(" ", "_")
        return text
    else:
        new_text = text.split("  ")
        final_text = ""
        for i in range(len(new_text)):
            if new_text[i] != "":
                final_text += new_text[i] + "-"
        final_text = final_text[:-1]
        return final_text
    
