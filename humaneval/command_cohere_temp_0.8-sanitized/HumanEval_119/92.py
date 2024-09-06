def match_parens(lst):
    cnt_open = 0
    for char in lst[1]:
        if char == '(':
            cnt_open += 1
        elif char == ')':
            cnt_open -= 1
        if cnt_open < 0:
            return "No"
    if cnt_open == 0:
        return "Yes"
    else:
        return "No"