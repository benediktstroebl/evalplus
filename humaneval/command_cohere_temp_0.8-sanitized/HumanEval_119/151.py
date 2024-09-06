def match_parens(lst):
    # Use a counter to keep track of open parentheses
    cnt = 0

    for char in lst[0] + lst[1]:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1

        if cnt < 0:  # Unbalanced
            return 'No'

    return 'Yes'