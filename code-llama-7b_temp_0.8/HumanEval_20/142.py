from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Is the list empty? If so, raise an error
    if len(numbers) == 0:
        raise ValueError("Empty list!")
    # Is the list just one element? If so, raise an error
    elif len(numbers) == 1:
        raise ValueError("List must contain at least two numbers")
    # Is the list more than one element? If so, continue
    else:
        # Initialize variables
        distance_first_num = float('inf')
        distance_second_num = float('inf')
        num_first = float('inf')
        num_second = float('inf')
        # Loop over each element in the list
        for i in range(len(numbers)):
            # If the first element has not been initialized yet, initialize it
            if i == 0:
                num_first = numbers[0]
                for j in range(len(numbers)):
                    if abs(numbers[j] - numbers[0]) < distance_first_num:
                        distance_first_num = abs(numbers[j] - numbers[0])
                        num_second = numbers[j]
                # Once the first number is initialized, update it with the next closest value
                for j in range(len(numbers)):
                    if abs(numbers[j] - numbers[0]) < distance_second_num:
                        if abs(numbers[j] - numbers[0]) != distance_first_num:
                            distance_second_num = abs(numbers[j] - numbers[0])
                            num_second = numbers[j]
                # Then, return the two closest numbers
                return num_first, num_second
            # If the first element has been initialized, check to see if the current element is closer to it than the
            # previous element
            else:
                if abs(numbers[i] - num_first) < distance_first_num:
                    # If the current element is closer to the first element than the previous element, update the
                    # previous element with the current element
                    num_second = num_first
                    num_first = numbers[i]
                    distance_second_num = distance_first_num
                    distance_first_
