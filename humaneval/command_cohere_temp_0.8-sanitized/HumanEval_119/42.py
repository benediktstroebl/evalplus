def match_parens(lst):
    open_ptr = 0
    for ch in lst[1]:
        if ch == '(':
            open_ptr += 1
        elif ch == ')':
            open_ptr -= 1
        if open_ptr < 0:
            return "No"
    if open_ptr == 0:
        return "Yes"
    else:
        return "No"