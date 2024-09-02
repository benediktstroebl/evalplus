from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    buckets = bucketize_numbers(numbers)
    best_pair = None
    for k, bucket in enumerate(buckets):
        for i, num in enumerate(bucket):
            if i >= 1 and num == bucket[i - 1]:
                continue
            for j, elem in enumerate(bucket):
                if j >= i + 1:
                    break
                if j != i and abs(num - elem) < abs(num - best_pair[0]) and abs(num - elem) < abs(
                        best_pair[1] - num):
                    best_pair = (num, elem)
    return best_pair

