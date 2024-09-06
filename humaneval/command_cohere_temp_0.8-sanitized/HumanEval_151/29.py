def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list, while ignoring negative or non-integer numbers.
    
    Returns:
        int: The sum of squares of odd numbers, or 0 if the list is empty or contains only negative or non-integer numbers.
    """
    # Ensure the list is sorted to make the indexing operation consistent
    lst = sorted(lst)
    
    total = 0  # Initialize the total sum
    
    # Traverse the sorted list
    for num in lst:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            total += num ** 2
    
    return total