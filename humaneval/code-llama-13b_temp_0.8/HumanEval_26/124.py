from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # O(n) time and O(n) space
    unique_numbers = set()
    unique_number_list = []
    for number in numbers:
        if number in unique_numbers:
            continue
        unique_numbers.add(number)
        unique_number_list.append(number)
    return unique_number_list

    # O(nlog(n)) time and O(1) space
    # numbers.sort()
    # i = 0
    # while i < len(numbers) - 1:
    #     if numbers[i] == numbers[i + 1]:
    #         numbers.pop(i)
    #     else:
    #         i += 1
    # return numbers

