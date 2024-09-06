from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # return bool(filter(lambda x: (abs(x[0] - x[1]) < threshold),
    #                    map(lambda n1: (n1, next((n2 for n2 in numbers if n1 != n2 and n1 - threshold <= n2 <= n1 + threshold), None)),
    #                        numbers)))
    return bool(
        filter(
            lambda n1: any(
                [
                    (n1 - n2 < threshold) and (n1 - n2 > -threshold)
                    for n2 in numbers
                    if n1 != n2
                ]
            ),
            numbers,
        )
    )

