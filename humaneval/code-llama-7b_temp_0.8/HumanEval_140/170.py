
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
    # TODO: implement me

    # pass
    out = ''
    for i in range(len(text)-1):
        if text[i]==' ':
            out+='_'
        else:
            out+=text[i]
        if text[i]==' ':
            if text[i+1]==' ':
                out+='-'
    if text[-1]==' ':
        out+='_'
    else:
        out+=text[-1]
    return out

