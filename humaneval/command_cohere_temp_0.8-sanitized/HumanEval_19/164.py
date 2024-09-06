def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_string.split()
    # Convert string to list of integers, sort them, then convert them back to a string.
    sorted_numbers = ' '.join(str(num) for num in sorted(map(int, numbers)))
    return sorted_numbers