from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers.sort()
    if len(numbers) <= 1:
        return numbers
    else:
        max_num = numbers[-1]
        min_num = numbers[0]
        new_list = []
        for num in numbers:
            if (num - min_num) == 0:
                return numbers
            new_list.append((num - min_num) / (max_num - min_num))
        return new_list

