
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
    if not text:
        return ""
    res = []
    for i in text:
        if i != " ":
            res.append(i)
        else:
            res.append("_")
    res = "".join(res)
    res = res.split("  ")
    for i in range(len(res)):
        if res[i].count(" ") > 1:
            res[i] = "-".join(res[i].split())
    res = "_".join(res)
    if res[0] == "_":
        res = res[1:]
    return res
