def match_parens(lst):
    # initialize the parentheses count
    count = 0
    
    for char in lst[0] + lst[1]:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # check if parentheses are balanced
                return 'No'
            
    return 'Yes'