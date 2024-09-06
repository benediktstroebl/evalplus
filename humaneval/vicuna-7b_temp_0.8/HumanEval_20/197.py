from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return numbers

    best_sum = numbers[0]
    best_other_sum = numbers[0]
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            other_sum = numbers[i] + numbers[j]
            if other_sum < best_sum:
                best_sum = other_sum
                best_other_sum = numbers[j]
            elif other_sum > best_sum:
                best_sum = other_sum
                best_other_sum = numbers[i]
            elif other_sum == best_sum:
                if j - i > 1:
                    break
        if i == len(numbers) - 1:
            break

    return best_sum, best_other_sum

