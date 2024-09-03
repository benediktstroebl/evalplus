from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Sorting elements is essential for proper sorting
    numbers = sorted(numbers)

    close_to_one_threshold: Dict[float, List[float]] = {}
    for i, number in enumerate(numbers):
        if number < threshold:
            continue
        close = sorted([number - number / 2, number + number / 2])
        for j, close_to_one_threshold in enumerate(close_to_one_threshold):
            if close_to_one_threshold < close[j]:
                close_to_one_threshold[close[j]] = [i]
                close_to_one_threshold.pop(close[j])
                break

    close_to_one_threshold = sorted(close_to_one_threshold.items(), key=lambda x: x[0])

    # All numbers were closer to each other
    if len(close_to_one_threshold) == 0:
        return True

    # All numbers were closer to each other by more than threshold
    if len(close_to_one_threshold) == 1:
        return close_to_one_threshold[0][0]

    # Some numbers aren't closer to each other
    not_close_to_one_threshold: List[int] = []
    for close_to_one_threshold in close_to_one_threshold:
        if len(close_to_one_threshold) == 1 and close_to_one_threshold[0][0] <= threshold:
            # Some numbers are closer to each other
            return close_to_one_threshold[0][0]
        if len(close_to_one_threshold) == 2 and close_to_one_threshold[0][0] <= threshold and close_to_one_threshold[0][1] <= threshold:
            # Two numbers are closer to each other
            return close_to_one_threshold[0][0]
        # Two numbers are not closer to each other
        not_close_to_one_threshold.append(close_to_one_threshold[0])

    # Number wasn't closer to any other number than threshold
    if len(not_close_to_one_threshold) == 0:
        return False

    # Number wasn't closer to any other number than threshold
    if len(not_close_to_one_threshold) == 1:
        return not_close_to_one_threshold[0][0]

    # Number wasn't closer to any other number than threshold and one number was already used
    if len(not_close_to_one_threshold) == 2:
        return not_close_to_one_threshold[0]

    # Number wasn't closer to any other number than threshold and two numbers were already used
    if len(not_close_to_one_threshold) == 3:
        return not_close_to_one_threshold[0]

