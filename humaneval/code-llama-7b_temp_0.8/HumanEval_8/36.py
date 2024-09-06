from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # zipped = [(1, 2), (3, 4)]
    # list(zip(*zipped))
    # [(1, 3), (2, 4)]
    # list(map(sum, list(zip(*zipped))))
    # [4, 6]
    # sum_p = list(map(sum, list(zip(*zipped))))
    # return (sum_p[0], sum_p[1])
    # return tuple(map(sum, zip(*((x,) * len(numbers) for x in numbers))))
    # return tuple(map(sum, zip(*map(lambda x: (x,) * len(numbers), numbers))))
    # return tuple(map(sum, zip(*map(lambda x: (x,) * len(numbers), numbers))))

    if len(numbers) == 0:
        return (0, 1)
    # if numbers == 0:
    #     return (0, 1)

    return tuple(map(sum, zip(*map(lambda x: (x,) * len(numbers), numbers))))

    # return tuple(sum(i) for i in zip(*[numbers for _ in range(len(numbers))]))

    # sum_p = [0, 1]
    # for n in numbers:
    #     sum_p[0] += n
    #     sum_p[1] *= n
    # return tuple(sum_p)

    # sum_p = [0, 1]
    # for n in numbers:
    #     sum_p[0] += n
    #     sum_p[1] *= n
    # return tuple(sum_p)

