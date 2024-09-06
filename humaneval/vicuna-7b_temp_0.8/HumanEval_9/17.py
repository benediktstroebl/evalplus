from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Find the current maximum element
    max_element = numbers[0]
    running_max_element = max_element

    # Initialize the number of elements that are being considered
    considered_elements = 0

    # Initialize the result list
    result = [running_max_element]

    # Loop over the list of elements
    for i in range(len(numbers)):
        # If the current element is greater than the current maximum element, update the maximum element
        if numbers[i] > running_max_element:
            running_max_element = numbers[i]
            max_element = running_max_element

        # If the current element is greater than the current maximum element and it is the first time it is considered,
        # add it to the result list
        if i == 0 and numbers[i] > running_max_element:
            considered_elements += 1
            result.append(numbers[i])

            # If the current element is greater than the current maximum element and it is the first time it is considered,
            # increment the number of elements being considered
            if considered_elements == 1:
                considered_elements = 0
            else:
                considered_elements -= 1

        # If the current element is the current maximum element, increment the number of elements being considered
        # and add the current maximum element to the result list
        if i == len(numbers) - 1:
            considered_elements = 0
            result.append(running_max_element)

    # Remove any duplicate elements from the result list
    return list(set(result))

