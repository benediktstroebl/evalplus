from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def replace_space(str1):
        return str1.replace(' ', '')

    def get_letters(str1):
        return list(str1)

    def convert_to_int(str1):
        list1 = []
        for i in range(len(str1)):
            list1.append(int(str1[i]))
        return list1

    def sort_list(list1):
        list1.sort()
        return list1

    def replace_letter(str1):
        str1 = str1.replace('0', 'zero')
        str1 = str1.replace('1', 'one')
        str1 = str1.replace('2', 'two')
        str1 = str1.replace('3', 'three')
        str1 = str1.replace('4', 'four')
        str1 = str1.replace('5', 'five')
        str1 = str1.replace('6', 'six')
        str1 = str1.replace('7', 'seven')
        str1 = str1.replace('8', 'eight')
        str1 = str1.replace('9', 'nine')
        return str1

    numbers_list = replace_space(numbers)
    numbers_list = get_letters(numbers_list)
    numbers_list = convert_to_int(numbers_list)
    numbers_list = sort_list(numbers_list)
    return replace_letter(str(numbers_list))

