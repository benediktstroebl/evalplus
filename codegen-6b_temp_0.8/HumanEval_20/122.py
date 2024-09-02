from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    # Find the minimum number of elements in the list
    min_elements = n // 2
    if n % 2 == 1:
        # Even
        l1 = numbers[:min_elements]
        l2 = numbers[n - min_elements:]
    else:
        # Odd
        l1 = numbers[:min_elements - 1]
        l2 = numbers[n - min_elements:]
    # Sort these lists in non-descending order
    l1_sorted = [a for a in sorted(l1)]
    l2_sorted = [a for a in sorted(l2)]
    # Find the largest difference and the smallest difference
    diff = abs(l1_sorted[-1] - l2_sorted[0])
    smallest = l1_sorted[-1]
    largest = l2_sorted[0]
    if diff == 0:
        return (smallest, largest)
    else:
        # Find the smallest and largest differences between the two lists
        smallest_diff = abs(l1_sorted[-1] - l2_sorted[0])
        largest_diff = abs(l1_sorted[-1] - l2_sorted[-1])
        # Select the smallest of these differences
        if smallest_diff <= largest_diff:
            return (smallest, l2_sorted[0])
        else:
            return (l1_sorted[-1], largest)

