from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)"""
    numbers.sort(numerical_order(numbers))
    min_distance = 100000000
    min_index = 0
    max_index = len(numbers) - 1

    for index in range(1, len(numbers)):
        distance = numbers[index - 1] - numbers[index]
        if distance < min_distance:
            min_distance = distance
            min_index = index

    if min_index < max_index:
        closest_num = numbers[min_index]
        furthest_num = numbers[max_index]
        return min_index, closest_num, furthest_num
    else:
        return -1, None, None