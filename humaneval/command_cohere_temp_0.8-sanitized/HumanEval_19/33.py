def sort_numbers(input_str: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    num_list = [char for char in input_str.replace(' ', '') if char in 'zero nine']
    num_list.sort()
    return ' '.join(num_list)