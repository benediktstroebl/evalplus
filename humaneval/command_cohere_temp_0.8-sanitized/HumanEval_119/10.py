def match_parens(lst):
    # Initialize the parentheses count for each variant
    count1 = 0
    count2 = 0
    
    for char in lst[0]:
        if char == '(':
            count1 += 1
        elif char == ')':
            count1 -= 1
    
    for char in lst[1]:
        if char == '(':
            count2 += 1
        elif char == ')':
            count2 -= 1
    
    # Check if the two strings can form a balanced one
    if max(count1, count2) == 0:
        return "Yes"
    
    return "No"