
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
    # fix_spaces("Example") == "Example"
    # fix_spaces("Example 1") == "Example_1"
    # fix_spaces(" Example 2") == "_Example_2"
    # fix_spaces(" Example   3") == "_Example-3"
    # fix_spaces(" Example 1 2 3 4") == "_Example_1_2_3_4"
    # fix_spaces("Example 1a2b3c") == "Example_1a2b3c"
    # fix_spaces("Example 1a2b3c ") == "Example_1a2b3c_"
    # fix_spaces("Example 1a2b3c    ") == "Example_1a2b3c-"
    # fix_spaces(" Example 1a2b3c") == "_Example_1a2b3c"


    string_to_fix = text
    # You should use the string split and join methods
    #to fix the spaces
    # string_to_fix = " ".join(string
