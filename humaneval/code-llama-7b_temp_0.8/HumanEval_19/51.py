from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Convert string to list
    numbers_list = numbers.split()
    # Set base case to first element
    sorted_list: List[str] = [numbers_list[0]]
    # Remove base case
    del numbers_list[0]

    # Loop through the list
    for number in numbers_list:
        # Loop through the sorted list
        for position, sorted_number in enumerate(sorted_list):
            # If the current number is smaller than the sorted number
            if number < sorted_number:
                # Insert the current number at the position
                sorted_list.insert(position, number)
                break
            # If the current number is not smaller than the sorted number and is not largest
            if number >= sorted_number and position != (len(sorted_list) - 1):
                continue
            # If the current number is not smaller than the sorted number and is the largest
            else:
                sorted_list.append(number)
                break

    return ' '.join(sorted_list)

