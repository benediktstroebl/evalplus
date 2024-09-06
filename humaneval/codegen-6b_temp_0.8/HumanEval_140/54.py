
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
    out = text
    if text == "":
        return ""
    out = ("_".join(out.split()))
    if out[0] == '_':
        out = out[1:]
    if not out == text:
        out = out.replace(" ", "_")
    if out[-1] == '_':
        out = out[:-1]
    return out
