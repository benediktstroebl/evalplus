from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Approach 1: Use python libraries
    # 
    # Approach 2: Brute Force
    #   Iterate through all the pairs of numbers and find one with the smallest difference.
    #   Use min() function to get the smallest difference from the list of differences
    #   between all the pairs
    # Approach 3: Sorting
    #   Sort the list of numbers in ascending order and find the closest pair
    # Approach 4: Divide and Conquer
    #   Divide the list of numbers into two halves, recursively find the closest pair of the two halves
    #   and then combine the results.
    # Approach 5: Sliding Window
    #   Use two pointers (low and high) into the list of numbers and find the closest pair.
    #   The closest pair is present in either of the following two cases:
    #     (a) The pair with numbers[low] and numbers[low + 1] (increasing)
    #     (b) The pair with numbers[high] and numbers[high - 1] (decreasing)
    #   Determine which of these two cases is better and adjust the two pointers appropriately.
    # 
    # NOTE: The complexity of all these approaches are the same (O(n))
    #
    # TODO: Implement your solution here
    pass

