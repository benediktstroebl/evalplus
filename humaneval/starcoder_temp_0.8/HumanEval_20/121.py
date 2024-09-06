from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    result = [0, 1]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                continue
            elif numbers[i] > numbers[j]:
                if numbers[result[0]] < numbers[i] and numbers[result[0]] < numbers[j]:
                    result[0] = i
                    result[1] = j
            elif numbers[i] < numbers[j]:
                if numbers[result[0]] > numbers[i] and numbers[result[0]] > numbers[j]:
                    result[0] = i
                    result[1] = j
    return numbers[result[0]], numbers[result[1]]

