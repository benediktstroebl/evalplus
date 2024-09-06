
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

    # write your code here
    fix_string = ""
    for word in text:
        if word != " ":
            fix_string = fix_string + word
        else:
            if fix_string[-1] == " ":
                fix_string += " "
            else:
                if fix_string[-1] == "-":
                    fix_string += "-"
                else:
                    fix_string += "_"

    return fix_string
