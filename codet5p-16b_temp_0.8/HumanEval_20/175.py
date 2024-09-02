from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest = float('inf')
    second_smallest = float('inf')

    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            if abs(numbers[i] - numbers[i + 1]) < smallest:
                smallest = abs(numbers[i] - numbers[i + 1])
                first_smallest = numbers[i]
                second_smallest = numbers[i + 1]
            elif abs(numbers[i] - numbers[i + 1]) == smallest:
                if numbers[i] < second_smallest:
                    second_smallest = numbers[i]
                    first_smallest = numbers[i + 1]
    return (first_smallest, second_smallest)

