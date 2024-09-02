from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_first, min_second = numbers[0], numbers[1]
    min_first_index, min_second_index = 0, 1
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!= j:
                first, second = numbers[i], numbers[j]
                if first < second:
                    if min_first_index == 0 and min_second_index == 1:
                        min_first = first
                        min_first_index = i
                        min_second = second
                        min_second_index = j
                    elif min_first < second:
                        min_second = second
                        min_second_index = j
                else:
                    if min_first_index == 0 and min_second_index == 1:
                        min_first = first
                        min_first_index = i
                        min_second = second
                        min_second_index = j
                    elif min_first > second:
                        min_second = second
                        min_second_index = j
    return (min_first, min_
