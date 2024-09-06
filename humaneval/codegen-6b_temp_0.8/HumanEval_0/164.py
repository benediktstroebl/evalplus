from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Find nodes that are closer to each other than threshold
    close_nodes = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                close_nodes.append((numbers[i], numbers[j]))
            elif numbers[j] - numbers[i] < threshold:
                close_nodes.append((numbers[j], numbers[i]))

    return len(close_nodes) > 0

