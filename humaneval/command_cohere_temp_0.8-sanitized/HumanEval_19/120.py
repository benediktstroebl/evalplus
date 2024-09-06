def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings comprised of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    # Sort function expects list of integers, so cast each string to int first.
    sorted_numbers = sorted(int(num) for num in numbers)
    return ' '.join(sorted_numbers)