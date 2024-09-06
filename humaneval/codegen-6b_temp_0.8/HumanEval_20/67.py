from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    sorted_numbers = numbers[:]
    sorted_numbers.sort()
    if sorted_numbers[0] == sorted_numbers[1]:
        sorted_numbers.sort()
        return sorted_numbers[0], sorted_numbers[1]
    ans = [sorted_numbers[0], sorted_numbers[1]]
    old_difference = abs(sorted_numbers[0] - sorted_numbers[1])
    new_difference = abs(sorted_numbers[2] - sorted_numbers[3])
    smallest = sorted_numbers[0]
    if new_difference < old_difference:
        smallest = sorted_numbers[3]
    for i in range(2, len(numbers)):
        new_difference = abs(numbers[i] - smallest)
        if new_difference < old_difference:
            old_difference = new_difference
            ans[0] = smallest
            ans[1] = numbers[i]
            smallest = ans[1]
    return tuple(ans)

