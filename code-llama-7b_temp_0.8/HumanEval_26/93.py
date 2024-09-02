from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # 1st solution:
    # sort list
    # then create a new list of unique values
    # runtime: O(nlog(n))
    numbers.sort()
    result = []
    for number in numbers:
        if not result or result[-1] != number:
            result.append(number)
    return result

    # 2nd solution:
    # use a set to check whether the number is in the set
    # run time: O(n)
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

    # 3rd solution:
    # create a dictionary (to keep track of the frequency of numbers)
    # runtime: O(n)
    num_freq = dict()
    for number in numbers:
        if number in num_freq:
            num_freq[number] += 1
        else:
            num_freq[number] = 1
    result = []
    for number in numbers:
        if num_freq[number] == 1:
            result.append(number)
    return result

