def match_parens(lst):
    # Use a counter to keep track of open parentheses
    counter = [0] * 2

    # Loop through each character in the strings
    for char in lst:
        if char == '(':
            counter[0] += 1
        else:
            counter[1] += 1

    # Check if the total number of open parentheses is equal to the number of close parentheses
    if counter[0] == counter[1]:
        return "Yes"
    else:
        return "No"