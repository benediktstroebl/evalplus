from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # if the list is empty, return an empty list
    if not numbers:
        return []

    # initialize the result list with the first element of the input list
    result = numbers[0]

    # initialize the count of max elements in the rolling window
    count = 1

    # initialize the rolling window with the first element of the input list
    window = numbers[0]

    # iterate over the rest of the input list
    for num in numbers[1:]:
        # if the current element is greater than the rolling window, update the rolling window and count
        if num > window:
            window = num
            count = 1
        # if the current element is less than or equal to the rolling window, increment the count and update the rolling window
        else:
            count += 1
            window = max(window, num)

    # return the result list with the number of max elements in the rolling window
    return [result] + [count] * (len(numbers) - len(result)) + [window]
