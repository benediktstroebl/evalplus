def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers without considering the starting or ending 1, then subtracts the
    # numbers that have a 1 in both positions to avoid double-counting.
    totals = [num * 2 - 1 for num in range(n, 0, -1)]
    
    # The list compuation expression `[x for x in totals if x >= 0]` 
    # generates a list containing only the positive numbers from the totals list.
    return sum([x for x in totals if x >= 0])