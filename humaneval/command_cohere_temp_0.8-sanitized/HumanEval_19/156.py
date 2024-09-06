def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_string.split()
    sorted_numbers = 'zero' in numbers + 'one' in numbers + 'two' in numbers + 'three' in numbers + 'four' in numbers + \
                        'five' in numbers + 'six' in numbers + 'seven' in numbers + 'eight' in numbers + 'nine' in numbers
    return ' '.join(sorted(numbers)) if sorted_numbers else input_string