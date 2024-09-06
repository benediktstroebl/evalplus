def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list, while ignoring negative or non-integer numbers.
    
    Returns:
        int: The sum of squares of odd numbers, or 0 if the list is empty or contains only even or negative numbers.
    """
    result = 0
    # Initialize a flag to track if any valid odd number is found.
    found_valid_odd = False
    
    # Iterate through the list and square each number.
    for num in lst:
        num = abs(num)  # Ensure num is not negative
        if num % 2 == 0:
            # If the number is even, skip squared calculation and continue.
            continue
        else:
            # If the number is odd, square it, and add the result to the total.
            result += num ** 2
            found_valid_odd = True
    
    # If no valid odd numbers were found, return 0.
    if not found_valid_odd:
        return 0
    
    return result