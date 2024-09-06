from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Find the lengths of the lists
    list_length = len(numbers)

    # Find the min and max values of the lists
    max_value = max(numbers)
    min_value = min(numbers)

    # Find the difference between the max and min values
    list_difference = max_value - min_value

    # Create two new lists for each of these differences
    list_1_difference = [0] * list_length
    list_2_difference = [0] * list_length

    # Fill the two newly created lists with the appropriate differences
    for i in range(list_length):
        list_1_difference[i] = abs(numbers[i] - min_value)
        list_2_difference[i] = abs(numbers[i] - max_value)

    # Find the minimum and maximum of the two differences
    min_1 = min(list_1_difference)
    max_1 = max(list_1_difference)
    min_2 = min(list_2_difference)
    max_2 = max(list_2_difference)

    # Find the indices of the min and max values
    index_1 = list_1_difference.index(min_1)
    index_2 = list_2_difference.index(max_2)

    # If the min difference is greater than the max difference, swap the two
    if min_1 > max_2:
        temp = index_1
        index_1 = index_2
        index_2 = temp

    # Add the max difference to the index_1 of the list
    numbers[index_1] = numbers[index_1] + list_difference

    # Add the min difference to the index_2 of the list
    numbers[index_2] = numbers[index_2] - list_difference

    # Return the two elements
    return (numbers[index_1], numbers[index_2])

