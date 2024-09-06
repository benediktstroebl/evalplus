def by_length(arr):
    DIGITS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
    
    # Sort and reverse the array
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]
    
    # Replace digits with their names
    result = [DIGITS.get(str(digit), 'Unknown') for digit in reversed_arr if 1 <= digit <= 9]
    
    return result
arr = [2, 1, 1, 4, 5, 8, 2, 3]