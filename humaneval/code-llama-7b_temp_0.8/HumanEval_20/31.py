from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Method One: Using Min-Heap

    # import heapq
    #
    # heapq.heapify(numbers)
    # min1 = heapq.heappop(numbers)
    # min2 = heapq.heappop(numbers)
    # while numbers:
    #     min1 = min(min1, numbers[0])
    #     if min1 - min2 > numbers[0] - min1:
    #         min2 = heapq.heappop(numbers)
    #     else:
    #         break
    # return min1, min2

    # Method Two: Using the list built-in min() function

    # min1 = min(numbers)
    # min2 = min(numbers)
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] - numbers[j] < min1 - min2:
    #             min1, min2 = numbers[i], numbers[j]
    # return min1, min2

    # Method Three: Using sort() built-in function

    sorted_numbers = sorted(numbers)
    min1 = sorted_numbers[0]
    min2 = sorted_numbers[0]
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] - sorted_numbers[i - 1] < min1 - min2:
            min1, min2 = sorted_numbers[i - 1], sorted_numbers[i]
    return min1, min2

