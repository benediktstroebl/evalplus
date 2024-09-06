from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # numbers.sort()
    # start_index = 0
    # for i in range(1, len(numbers)):
    #     if numbers[start_index] != numbers[i]:
    #         start_index += 1
    #         numbers[start_index] = numbers[i]
    # return numbers[:start_index + 1]

    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

