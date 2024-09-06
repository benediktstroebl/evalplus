def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    Valid inputs are strings containing digits 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_str.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers