def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    Valid inputs are from 'zero' to 'nine'.
    Returns the sorted string.
    """
    num_list = input_str.strip().split(' ')
    num_list.sort()
    return ' '.join(num_list)