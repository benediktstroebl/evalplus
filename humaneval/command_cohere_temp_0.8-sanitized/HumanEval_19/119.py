def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings comprised of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    # Sort function expects list of integers, cast each string to int to sort, then revert to string
    sorted_numbers = [str(elem) for elem in sorted(map(int, numbers))]
    return ' '.join(sorted_numbers)