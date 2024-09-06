from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # First approach: brute force - O(n^2)
    # min_distance = float('inf')
    # answer = (0.0, 0.0)
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         distance = abs(numbers[i] - numbers[j])
    #         if distance < min_distance:
    #             min_distance = distance
    #             answer = (numbers[i], numbers[j])
    # return answer

    # Second approach: O(nlogn)
    numbers.sort()
    min_distance = numbers[-1] - numbers[0]
    answer = (numbers[0], numbers[-1])
    for i in range(len(numbers) - 1):
        distance = numbers[i + 1] - numbers[i]
        if distance < min_distance:
            min_distance = distance
            answer = (numbers[i], numbers[i + 1])
    return answer

