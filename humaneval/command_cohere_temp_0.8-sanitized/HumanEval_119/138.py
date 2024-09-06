def match_parens(lst):
    # Ensure that the first and last characters are ( and ) respectively
    if lst[0][0] == '(' and lst[-1][-1] == ')':
        ans = 'Yes'
    else:
        ans = 'No'
    
    # Check if one of the strings is just a pair of parentheses
    if len(lst) == 1:
        return ans
    
    # Check if one of the strings has just one parenthesis
    for i in lst:
        if len(i) == 1:
            return 'No'
    
    # Ensure that all other strings have even lengths and are balanced
    for i in lst:
        if len(i) % 2 != 0 or i.count('(') != i.count(')'):
            return 'No'
    
    return ans