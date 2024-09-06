from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # this is the check that is needed to implement a solution
    # O(nlogn) time, O(1) space
    # numbers.sort()
    # for i in range(len(numbers) - 1):
    #     if numbers[i+1] - numbers[i] < threshold:
    #         return True
    # return False

    # O(n^2) time, O(1) space
    # for i in range(len(numbers) - 1):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[j] - numbers[i] < threshold:
    #             return True
    # return False

    # O(n) time, O(1) space
    # smallest = smallest_diff = float("inf")
    # for i in range(len(numbers) - 1):
    #     difference = numbers[i+1] - numbers[i]
    #     if difference < smallest_diff:
    #         smallest_diff = difference
    #         smallest = numbers[i]
    # return smallest_diff < threshold

    # O(n) time, O(1) space
    # for i in range(len(numbers) - 1):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[j] - numbers[i] < threshold:
    #             return True
    # return False

    # O(n) time, O(1) space
    # smallest = smallest_diff = float("inf")
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         difference = abs(numbers[j] - numbers[i])
    #         if difference < smallest_diff:
    #             smallest_diff = difference
    #             smallest = numbers[i]
    # return smallest_diff < threshold

    # O(n) time, O(1) space
    # smallest = smallest_diff = float("inf")
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    
