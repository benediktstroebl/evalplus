
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
    s1=text.split()
    for i in range(len(s1)):
        if i==0:
            if s1[i]!='':
                s1[i]='_'+s1[i]
        else:
            s1[i]='_'+s1[i]
    for i in range(len(s1)):
        if i==0:
            if s1[i]!='':
                s1[i]=s1[i]
        else:
            if s1[i]!='' and s1[i-1]!='':
                s1[i]='_'+s1[i]
            else:
                s1[i]=s1[i]
    for i in range(len(s1)):
        if s1[i]!='':
            s1[i]='_'+s1[i]
        else:
            s1[i]=s1[i]
    return(''.join(s1))
