from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def sort(num: str, is_sorted: bool) -> str:
        """
        :param num: number in string
        :param is_sorted: if number string is sorted
        :return: number string in sorted order
        """
        if is_sorted:
            return num

        # convert string to list
        num_list = num.split(' ')
        sorted_num = ' '
        for num in num_list:
            sorted_num += next(numbers.sorted(key=num.lower)) + ' '

        return sorted_num

    return ' '.join(sort(num, False) for num in numbers.split(' '))

