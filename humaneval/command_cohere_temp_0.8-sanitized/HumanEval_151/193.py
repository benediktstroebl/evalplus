def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    # First, we handle the edge case where the input list is empty
    if not nums:
        return 0
    
    odd_nums = [num for num in nums if num % 2 and num >= 0]
    squared_odd = [num ** 2 for num in odd_nums]
    return sum(squared_odd)