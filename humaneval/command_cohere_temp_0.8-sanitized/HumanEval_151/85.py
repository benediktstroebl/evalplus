def double_the_difference(lst):
    result = 0

    # Filter out non-integer values and negative numbers
    valid_numbers = [num for num in lst if isinstance(num, int) and num >= 0]
    
    # Calculate the squares of valid odd numbers and sum them
    odd_numbers = [num for num in valid_numbers if num % 2 != 0]
    squared_odds = [num ** 2 for num in odd_numbers]
    result += sum(squared_odds)
    
    # Handle empty list case
    if not valid_numbers:
        return 0
    
    return result