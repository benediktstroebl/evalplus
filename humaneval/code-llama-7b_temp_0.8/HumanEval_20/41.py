from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # SOLUTION:
    # 1. First we will find the index of the smallest element, and then the largest element.
    # 2. We will then swap the index of the largest element with the last index of the array
    # (so that this last element is at the position of the smallest element).
    # 3. We will then compare the numbers before and after the position of the largest element
    # to see which is closer to the largest element. We will use the first element before the largest element
    # or the first element after the largest element (whichever is closer).

    # 1. Find index of the smallest element:
    smallest_element_index = numbers.index(min(numbers))

    # 2. Find index of the largest element:
    largest_element_index = numbers.index(max(numbers))

    # 3. Swap the largest element with the smallest element:
    numbers[largest_element_index], numbers[smallest_element_index] = numbers[smallest_element_index], numbers[largest_element_index]

    if smallest_element_index == len(numbers) - 1:
        smaller_element = numbers[smallest_element_index]
        larger_element = numbers[0]
    else:
        smaller_element = numbers[smallest_element_index + 1]
        larger_element = numbers[smallest_element_index - 1]

    return (smaller_element, larger_element)

