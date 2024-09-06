def match_parens(lst):
    close_count = [0, 0]
    for char in lst[1]:
        if char == '(':
            open_count = open_count + 1
        else:
            open_count = open_count - 1
        close_count[open_count] += 1
    if max(close_count) >= 1:
        return "Yes"
    else:
        return "No"