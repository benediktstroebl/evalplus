from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    def max_rolling(acc: Tuple[int, int], next_num: int) -> Tuple[int, int]:
        return (max(next_num, acc[0]), max(acc[1], acc[0] * next_num))

    return list(map(lambda x: x[1], reduce(max_rolling, numbers, (numbers[0], 0))))

