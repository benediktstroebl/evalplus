from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Create an empty list to store the close elements
    close_elements = []

    # Iterate over the numbers in the list
    for i in range(len(numbers) - 1):

        # Check if the absolute difference between the current and next number is less than
        # threshold
        if abs(numbers[i] - numbers[i + 1]) < threshold:

            # If there are already close elements in the list, check if the current number
            # is closer than any of the previous close elements
            if len(close_elements) > 0:
                if abs(numbers[i] - numbers[i + 1]) < abs(close_elements[-1] - numbers[i + 1]):
                    close_elements.append(numbers[i])

            # Otherwise, if the current number is not closer than any of the previous close
            # elements, add it to the list
            else:
                close_elements.append(numbers[i])

    # Check if there are any close elements in the list
    if len(close_elements) >
