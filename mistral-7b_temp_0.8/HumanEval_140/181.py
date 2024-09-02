
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
    # TODO: implement fix_spaces
    final_list = list(text)
    for i in range(len(final_list)):
        if final_list[i] == " ":
            if i + 1 == len(final_list):
                final_list[i] = "_"
            elif final_list[i + 1] == " ":
                final_list[i] = "-"
            else:
                final_list[i] = "_"
    return "".join(final_list)
