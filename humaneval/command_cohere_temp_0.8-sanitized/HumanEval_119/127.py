def match_parens(lst):
    open_ptr = 0
    for char in lst[1]:
        if char == '(':
            open_ptr += 1
        elif char == ')':
            open_ptr -= 1
        if open_ptr < 0:
            return "No"
    if open_ptr == 0:
        return "Yes"
    else:
        return "No"