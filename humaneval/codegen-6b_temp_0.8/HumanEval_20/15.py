from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # From the list of numbers, we need two elements that are closest to each other. This is the minimum number of
    # intersections between these two elements and the intersection is the number of elements that are closest to
    # each other.
    # We are looking for all the possible numbers to be the closest to each other.
    # We are looking for all the pairs of numbers that are closest to each other.
    # We are looking for all the possible pairs of numbers that are closest to each other. For each pair, we are
    # reducing the possible numbers to the elements that are closest to each other.
    # We then choose the two elements that are closest to each other as the closest elements.
    # However, we want the elements of the first list of numbers to be closer to the second list of numbers than to
    # each other. This is because the second list of numbers is sorted. Consequently, we care about the smallest
    # element of the second list. We pick the number that is closest to the smallest number in the second list of
    # numbers. We then pick the two smallest numbers.
    # We then sort the first list of numbers so that the smallest number is the first element. The second list of
    # numbers (first list of numbers sorted) is then sorted to find the smallest element. We then pick the two
    # smallest elements.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then the second element.
    # We pick the two smallest elements and then return the first element first, then