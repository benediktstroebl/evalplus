def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    Valid inputs are from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers