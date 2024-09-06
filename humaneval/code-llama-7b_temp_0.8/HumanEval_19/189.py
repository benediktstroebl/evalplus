from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # pattern = 'zero|one|two|three|four|five|six|seven|eight|nine'
    # output_text = ''
    # for word in numbers.split():
    #     if re.search(pattern, word):
    #         output_text += word + ' '
    # return output_text.strip()
    numbers = [ord(c)-97 for c in numbers]
    return ' '.join([word for word in numbers.sort()])

