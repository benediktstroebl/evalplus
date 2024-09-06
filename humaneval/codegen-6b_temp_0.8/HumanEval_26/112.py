from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) < 2:
        return numbers
    else:
        result_list = []
        # for i, n in enumerate(numbers):
        #     if numbers.count(n) > 1:
        #         continue
        #     else:
        #         result_list.append(n)
        #     i += 1

        result_list = [numbers[i] for i, n in enumerate(numbers) if numbers.count(n) == 1]
        return result_list

