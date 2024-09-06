def by_length(arr):
    """
    Sort digits from 1 to 9 in the array, reverse the sorted array, 
    and replace digits with their names. strangely numbered entries are ignored.

    Args:
        arr (list): List of integers containing potentially numeric entries.

    Returns:
        list: List of named digits in the format "One", "Two", ..., "Nine".

    """
    # Sort the array of integers from 1 to 9 and reverse it
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted_arr[::-1]
    
    # Convert each number in the reversed sorted array to its name
    named_digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [digit_name for digit_name, digit in zip(named_digits, reversed_sorted_arr) if digit in range(1, 10)]