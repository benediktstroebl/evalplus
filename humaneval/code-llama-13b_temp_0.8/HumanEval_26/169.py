from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Time Complexity: O(n^2)
    # for x in range(len(numbers) - 1):
    #     if numbers[x] == numbers[x + 1]:
    #         numbers.pop(x)
    # return numbers

    # Time Complexity: O(n^2)
    # seen = []
    # for x in range(len(numbers) - 1):
    #     if numbers[x] not in seen:
    #         seen.append(numbers[x])
    #     else:
    #         numbers.pop(x)
    # return numbers

    # Time Complexity: O(n)
    seen = set()
    unique_numbers = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)
    return unique_numbers
