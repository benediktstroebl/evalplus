def double_the_difference(lst):
    if not lst:  # Check if the list is empty
        return 0
    
    odd_numbers = [num for num in lst if num % 2 == 1]
    result = sum([num**2 for num in odd_numbers])
    return result