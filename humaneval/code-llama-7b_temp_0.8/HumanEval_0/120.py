from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # sort list
    sorted_numbers = sorted(numbers)

    # for each element in list
    for i in range(0, len(sorted_numbers) - 1):
        # get number
        num = sorted_numbers[i]

        # for each element that comes after
        for j in range(i + 1, len(sorted_numbers)):
            # get next number
            next_num = sorted_numbers[j]

            # calculate the difference between them
            diff = abs(num - next_num)

            # if difference is less than threshold return True
            if diff < threshold:
                return True

    # otherwise return False
    return False
