from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_length = len(numbers)

    if numbers_length < 2:
        raise ValueError("Numbers length must be greater than or equal to two.")

    lower_index = 0
    upper_index = numbers_length - 1

    lower_value = numbers[lower_index]
    upper_value = numbers[upper_index]

    while lower_index < upper_index:
        mid_index = (lower_index + upper_index) // 2
        mid_value = numbers[mid_index]

        if mid_value == lower_value:
            lower_index += 1
        elif mid_value == upper_value:
            upper_index -= 1
        else:
            if mid_value < lower_value:
                lower_index = mid_index
            elif mid_value > upper_value:
                upper_index = mid_index
            else:
                raise ValueError(
                    f"Mid value {mid_value} at index {mid_index} must not be equal to lower value {lower_value} "
                    f"or upper value {upper_value}."
                )

    lower_index -= 1
    upper_index += 1

    return numbers[lower_index], numbers[upper_index]

