from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # We have an algorithm that looks for the closest numbers.
    # We assume that the supplied list is at least two items long.
    # We use a variant of the binary search algorithm.
    #
    # We have a potential problem:
    # 1) We don't know the difference between two elements of the list.
    # 2) We don't know the difference between the elements.
    # 3) We don't know if the elements are in the right order.
    #
    # Our binary search will narrow the search space as it goes.
    # But we want to work with the original list, so we want to store the original sorted order of the list.
    #
    # Our algorithm may work with any number of elements.
    # We want to work with the original, so we sort the list before dealing with it.
    #
    # We know that the sequence of elements has to be "ordered" so the first index will be the closest to the last index.
    # So we sort in decreasing order of distance, and the first index is the closest to the last index.
    #
    # First, we want to know which elements are the closest to each other.
    # We can do this by comparing the differences between each element and the next elements.
    # We can do this by comparing the differences  between each element and the remaining elements.
    #
    # We can create a list of the differences between the current element and the remaining elements.
    #
    # If the element is the first element, we can use the next item to get the second difference between the first and
    # the second elements.
    #
    # If the element is the second element, we can use the previous element to get the first difference between the
    # second and the next elements.
    #
    # This approach works because the list is sorted in a decreasing order.
    # The element that is closest to itself is the element that is the second to the last index.
    #
    # The element that is closest to the next element is the element that is the second to the last index.
    #
    # What is the element that is the second to the last index?
    # What is the element that is the second to the last index?
    #
    # The second to the last index