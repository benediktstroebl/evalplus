from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # todo: Write your code here
    new_list = [0 for _ in range(len(numbers))]
    new_list[0] = 0
    new_list[1] = (numbers[1]-numbers[0])/(numbers[len(numbers)-1]-numbers[0])
    new_list[2] = (numbers[2]-numbers[0])/(numbers[len(numbers)-1]-numbers[0])
    new_list[3] = (numbers[3]-numbers[0])/(numbers[len(numbers)-1]-numbers[0])
    new_list[4] = (numbers[4]-numbers[0])/(numbers[len(numbers)-1]-numbers[0])
    new_list[5] = (numbers[5]-numbers[0])/(numbers[len(numbers)-1]-numbers[0])
    new_list[6] = (numbers[6]-numbers[0])/(numbers[len(
