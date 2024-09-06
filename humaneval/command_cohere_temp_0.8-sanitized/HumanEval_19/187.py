def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from shortest to longest.
    Valid input includes any number from 0-9 in word form ('zero', 'one', 'two', ..., 'nine').
    """
    numbers = input_string.split()
    # Sort the list of numbers (strings) into alphabetical order, which gives us the order from shortest to longest.
    sorted_numbers = sorted(numbers)
    return ' '.join(sorted_numbers)