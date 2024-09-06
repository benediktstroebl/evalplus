
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
    # return text.replace(" ","_").replace("  ","-").replace("   ","-")
    fixed = ""
    space_count = 0
    for c in text:
        if c == " ":
            space_count += 1
        else:
            if space_count >= 2:
                fixed += "-" * space_count
                space_count = 0
            fixed += c
    if space_count >= 2:
        fixed += "-" * space_count
        space_count = 0
    return fixed

