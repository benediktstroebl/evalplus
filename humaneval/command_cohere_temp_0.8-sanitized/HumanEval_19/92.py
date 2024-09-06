def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid input includes any combination of the numbers 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    numbers.sort()
    return ' '.join(numbers)