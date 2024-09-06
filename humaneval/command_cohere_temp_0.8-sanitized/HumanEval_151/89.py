def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    '''
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            if n % 2 == 1:
                result += n * n
        elif n == 0:
            result += 0  # Handle zero correctly
    return result