def match_parens(lst):
    # use a counter to track the number of open parentheses
    open_cnt = 0
    for char in lst[0]:
        if char == '(':
            open_cnt += 1
        elif char == ')':
            open_cnt -= 1
        if open_cnt < 0:
            return "No"
    lst[0] = ''.join(lst[0])
    lst[1] = ''.join(lst[1])
    if open_cnt != 0:
        return "No"
    return "Yes"