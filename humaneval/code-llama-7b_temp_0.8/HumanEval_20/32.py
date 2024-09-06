from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # get the smallest number in the list
    smallest = min(numbers)
    # get the largest number in the list
    largest = max(numbers)
    # get the index of smallest number
    smallest_index = numbers.index(smallest)
    # get the index of largest number
    largest_index = numbers.index(largest)
    # get the number at the next index of the smallest
    next_smallest = numbers[smallest_index + 1]
    # get the number at the previous index of the smallest
    previous_smallest = numbers[smallest_index - 1]
    # get the number at the next index of the largest
    next_largest = numbers[largest_index + 1]
    # get the number at the previous index of the largest
    previous_largest = numbers[largest_index - 1]
    # if the distance between the smallest and the next is smaller than the distance between the largest and the next
    if abs(numbers[smallest_index] - numbers[smallest_index + 1]) < abs(numbers[largest_index] - numbers[largest_index + 1]):
        return smallest, next_smallest
    # if the distance between the smallest and the next is greater than the distance between the largest and the next
    elif abs(numbers[smallest_index] - numbers[smallest_index + 1]) > abs(numbers[largest_index] - numbers[largest_index + 1]):
        return largest, next_largest
    # if the distance between the smallest and the previous is smaller than the distance between the largest and the previous
    elif abs(numbers[smallest_index] - numbers[smallest_index - 1]) < abs(numbers[largest_index] - numbers[largest_index - 1]):
        return smallest, previous_smallest
    # if the distance between the smallest and the previous is greater than the distance between the largest and the previous
    elif abs(numbers[smallest_index] - numbers[smallest_index - 1]) > abs(numbers[largest_index] - numbers[largest_index - 1]):
        return largest, previous_largest

