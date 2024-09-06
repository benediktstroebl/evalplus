def match_parens(lst):
    # Use a counter to track the number of open parentheses
    open_cnt = 0

    # Iterate through both strings
    for char in lst:
        if char == '(':
            open_cnt += 1
        elif char == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return "No"
    
    # If the total open parentheses count is zero, it's a valid string
    if open_cnt == 0:
        return "Yes"
    
    return "No"