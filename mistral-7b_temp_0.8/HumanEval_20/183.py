from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Test case for list size of 2
    if len(numbers) == 2:
        return (numbers[0], numbers[1])

    # Test case for list size of 3
    elif len(numbers) == 3:
        return (min(numbers), max(numbers))

    # Normal case, determine smallest number and largest number
    min_num = min(numbers)
    max_num = max(numbers)

    # Assign the distance between min and max to a variable
    distance = max_num - min_num

    # Create a list of all numbers from min_num to max_num (not including max_num)
    list_of_nums = [min_num + x for x in range(distance)]

    # Find the index of the nearest number in the list of numbers
    list_of_indexes = [(list_of_nums.index(x), x) for x in numbers]
    nearest_index = min(list_of_indexes, key=lambda x: abs(x[1] - min_num
