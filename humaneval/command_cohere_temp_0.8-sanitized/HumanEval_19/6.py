def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid inputs are strings containing digits from 0 to 9.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers