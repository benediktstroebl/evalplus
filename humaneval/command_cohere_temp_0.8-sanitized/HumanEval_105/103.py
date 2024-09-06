def by_length(arr):
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    odd_idx = -1
    even_idx = -1
    
    # Sort the array based on length, then reverse it
    sorted_arr = sorted(arr, key=lambda x: (len(str(x)), x))
    reversed_arr = sorted_arr[::-1]
    
    result = []
    for num in reversed_arr:
        if len(str(num)) % 2 == 0:
            result.append(DIGITS[even_idx])
            even_idx -= 1
        else:
            result.append(DIGITS[odd_idx])
            odd_idx -= 1
    
    return result if result else []