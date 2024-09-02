from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # To determine which number is closest, use the following formula:
    # delta = n1 - n2
    # if abs(delta) < abs(delta_old):
    #    delta_old = delta
    # delta_old = delta
    # i = 0
    # if delta > 0:
    #    for i in range(len(numbers)):
    #        if numbers[i] > numbers[i - 1]:
    #            break
    # elif delta < 0:
    #    for i in range(len(numbers)):
    #        if numbers[i] < numbers[i - 1]:
    #            break
    # delta = numbers[i] - numbers[i - 1]

    # Find the two closest numbers
    # - Use python's indexing to find the index of the smallest and largest number
    smallest_index = 0
    smallest_number = abs(numbers[0] - numbers[1])
    for i in range(len(numbers)):
        if abs(numbers[i] - numbers[0]) < smallest_number:
            smallest_index = i
            smallest_number = abs(numbers[i] - numbers[0])

    largest_index = 0
    largest_number = abs(numbers[0] - numbers[1])
    for i in range(len(numbers)):
        if abs(numbers[i] - numbers[0]) > largest_number:
            largest_index = i
            largest_number = abs(numbers[i] - numbers[0])

    # - Use a pair of variables to track the smallest and largest number
    # - Assign the first number to the smallest
    # - If the first number is larger than the second, swap them
    # - If the first number is smaller than the second, swap them
    # - Loops over the remaining numbers and compares the first number to the second
    # - If the first number is closer to the second, swap them
    # - Return the two closest numbers
    # - Maintain an ordering in which the number is closest to the first number
    # - Return the tuple of two closest numbers in sorted order
    smallest_number = numbers[small