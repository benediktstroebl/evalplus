from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # assert type(numbers) == list
    # assert all(type(n) == int for n in numbers)
    # # 1. find number of unique numbers
    # # 2. remove duplicates from input list
    # # 3. return result
    #
    # unique_numbers = set(numbers)
    #
    # for num in unique_numbers:
    #     numbers.remove(num)
    #
    # return numbers
    # # your code here
    #
    # # your code here
    # unique_numbers = set(numbers)
    #
    # for num in unique_numbers:
    #     numbers.remove(num)
    #
    # return numbers

    # your code here
    unique_numbers = set(numbers)

    return list(unique_numbers)

