from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Efficient solution
    # O(n)

    # a = min(numbers, key=abs)
    # return min([(a, b) for b in numbers if b != a], key=lambda x: x[1] - x[0])

    # Simple solution
    # O(n^2)
    #
    # for i in range(len(numbers)):
    #     a = numbers[i]
    #     for j in range(i + 1, len(numbers)):
    #         b = numbers[j]
    #         if abs(a - b) < abs(a - min(numbers, key=abs)) and abs(a - b) < abs(min(numbers, key=abs) - b):
    #             return a, b

    # Optimized solution
    # O(n)
    #
    # a, b = min([(a, b) for a in numbers for b in numbers if a < b], key=lambda x: x[1] - x[0])
    # return a, b

    # Simplified optimized solution
    # O(n)
    #
    # a, b = min((a, b) for a in numbers for b in numbers if a < b), max((a, b) for a in numbers for b in numbers if a > b)
    # return a[0], b[0]

    # Simplified optimized solution
    # O(n)
    #
    # a, b = min((a, b) for a in numbers for b in numbers if a < b), min((a, b) for a in numbers for b in numbers if a > b)
    # return a[0], b[0]

    return min(((a, b) for a in numbers for b in numbers if a < b), key=lambda x: x[1] - x[0])

