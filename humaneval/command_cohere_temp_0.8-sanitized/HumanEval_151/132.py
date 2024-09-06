def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Input: lst ([1, 3, 2, 0])
    Output: 10
    Explanation: 1 is odd, 3 is odd, 2 is even, 0 is both even and not an integer. sum up: 1^2 + 3^2 + 0 + 0 = 1 + 9 + 0 + 0 = 10
    """
    result = 0
    for num in lst:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result