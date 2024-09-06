def match_parens(lst):
    # Use a counter to keep track of opening parentheses
    counter = 0

    for char in lst[0] + lst[1]:
        if char == '(':
            counter += 1
        else:
            counter -= 1

        if counter < 0:  # Unbalanced
            return "No"

    return "Yes"