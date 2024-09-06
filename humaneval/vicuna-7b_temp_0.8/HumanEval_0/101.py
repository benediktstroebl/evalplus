from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # convert numbers to cents
    cent_numbers = [round(num * 100) for num in numbers]

    # check if any two numbers are closer than threshold
    closest_distance = float('inf')
    closest_pair = None
    for i in range(len(cent_numbers)):
        for j in range(i + 1, len(cent_numbers)):
            distance = abs(cent_numbers[i] - cent_numbers[j])
            if distance < closest_distance or (distance == closest_distance and cent_numbers[i] < cent_numbers[j]):
                closest_distance = distance
                closest_pair = (cent_numbers[i], cent_numbers[j])

    return closest_pair is not None and closest_distance < threshold

