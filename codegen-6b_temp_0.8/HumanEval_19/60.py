from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the string into words
    words = numbers.split(' ')
    # Create a list to store the numbers
    numbers = []
    # Iterate through the string backwards, then backwards one more time
    for word in words[::-1]:
        # If the word is a numberical word, add it to the numbers list
        if word.isdigit():
            numbers.append(int(word))
    # Sort the numbers
    numbers.sort()
    # Join the numbers back into a string
    return ' '.join([str(number) for number in numbers][::-1])

