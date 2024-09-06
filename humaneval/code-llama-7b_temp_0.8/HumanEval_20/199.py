from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # initialize list of the number closest to the number at index 0 of the number list
    numbers_closest = [numbers[0]]
    # loop through each element of the number list
    for number in numbers:
        # if the number is less than the number at index 0 of the number list
        if number < numbers[0]:
            # if the number is greater than the first number in the list of closest numbers
            if number > numbers_closest[0]:
                # append the number to the end of the list of closest numbers
                numbers_closest.append(number)
        # if the number is greater than the number at index 0 of the number list
        elif number > numbers[0]:
            # if the number is less than the first number in the list of closest numbers
            if number < numbers_closest[0]:
                # insert the number into the first index of the list of closest numbers
                numbers_closest.insert(0, number)
            # if the number is equal to the first number in the list of closest numbers
            elif number == numbers_closest[0]:
                # append the number to the end of the list of closest numbers
                numbers_closest.append(number)
    # if the length of the list of closest numbers is equal to 1
    if len(numbers_closest) == 1:
        # select the number at index 0 in the list of closest numbers
        closest_1 = numbers_closest[0]
        # select the number at index 1 in the list of closest numbers
        closest_2 = numbers_closest[0]
    # if the length of the list of closest numbers is equal to 2
    elif len(numbers_closest) == 2:
        # select the number at index 0 in the list of closest numbers
        closest_1 = numbers_closest[0]
        # select the number at index 1 in the list of closest numbers
        closest_2 = numbers_closest[1]
    # return the number that is smaller, and the number that is larger
    return min(closest_1, closest_2), max(closest_1, closest_2)

