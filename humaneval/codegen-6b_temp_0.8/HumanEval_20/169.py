from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Quick out-of-place comparison and swap if they are not close
    comparisons = 0
    n_size = len(numbers)
    while comparisons < n_size - 1:
        comparisons += 1
        smallest = numbers[0]
        largest = numbers[0]
        for i in range(1, n_size):
            comparisons += 1
            if smallest > numbers[i]:
                smallest = numbers[i]
                numbers[i], numbers[0] = numbers[0], numbers[i]
            elif smallest < numbers[i]:
                smallest = numbers[i]
            if largest < numbers[i]:
                largest = numbers[i]
                numbers[i], numbers[0] = numbers[0], numbers[i]
            elif largest > numbers[i]:
                largest = numbers[i]
        if abs(smallest - numbers[0]) < abs(largest - numbers[0]):
            numbers[0], numbers[1] = numbers[1], numbers[0]
        else:
            numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers[0], numbers[1]

