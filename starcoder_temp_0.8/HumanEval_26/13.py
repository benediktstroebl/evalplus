from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # def aux(num, result):
    #     if len(num) == 0:
    #         return result

    #     if num[0] not in result:
    #         result.append(num[0])

    #     return aux(num[1:], result)

    # return aux(numbers, [])

    return list(set(numbers))

