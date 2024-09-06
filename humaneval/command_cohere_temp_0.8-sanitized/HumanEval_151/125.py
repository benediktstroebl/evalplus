def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    If the input list is empty, return 0.
    
    Examples:
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    """
    # Check if the list is empty
    if not lst:
        return 0
    
    # Initialize sum to store the result
    sum_result = 0
    
    # Iterate over the list and check if each number is odd, positive, and an integer
    for num in lst:
        if num % 2 != 0 and num > 0 and isinstance(num, int):
            sum_result += num ** 2
    
    return sum_result