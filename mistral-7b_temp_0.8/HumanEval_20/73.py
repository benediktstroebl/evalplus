from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Your code here
    # print(numbers)

    # find the smallest value
    min_value = min(numbers)
    # print(min_value)

    # find the index of the smallest value
    min_index = numbers.index(min_value)
    # print(min_index)

    # set the first index to the minimum
    number1 = numbers[min_index]
    # print(number1)

    # if the second index is the minimum, set the first index to that and the third index to the minimum
    if min_index == 0:
        number2 = numbers[1]
        number3 = min_value
    # if the second index is not the minimum, set the second index to the minimum and the third index to the second index
    elif min_index == 1:
        number2 = min_value
        number3 = numbers[2]
    # if the second index is not the minimum, set the second index to the minimum and the third index to the third index
    else:
        number2 = min_value
        number3 = numbers
