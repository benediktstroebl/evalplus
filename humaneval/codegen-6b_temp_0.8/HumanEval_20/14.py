from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # We can solve this problem using 2 lists - one of the smaller elements and one of the larger elements.
    # We could think of the smaller element as being the one that has the smaller distance from the larger element
    # and the larger element as being the one that has the larger distance from the smaller element.
    # To do this we'll need to sort the list first so that the smallest element is first
    # and the largest element is last.
    # What we'll do is traverse the array from start to the end and compare the number against the two elements
    # before and after the current number. If the current number is closer to the before or after number compared to
    # the current element then we change the current element in the result tuple. Once the current element is not
    # beig the result, we return the result.
    small = [1e10, -1]
    large = [-1e10, 1]
    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i] < small[0]:
            small = [numbers[i], numbers[i - 1]]
        elif numbers[i - 1] > numbers[i] > large[0]:
            large = [numbers[i], numbers[i - 1]]
    return small[0], large[1]

