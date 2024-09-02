from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    m = len(numbers)
    vecs = [
        [0 for _ in range(m + 1)] for _ in range(m + 1)
    ]  # initializing matrix
    # filling matrix
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if numbers[i - 1] > numbers[j - 1]:
                vecs[i][j] = vecs[i - 1][j] + 1
            else:
                vecs[i][j] = vecs[i - 1][j - 1]
    # filling vertices
    vertices = []
    for i in range(m + 1):
        try:
            vertices.append(vecs[i][m])
        except IndexError:
            # trying to do matrix[m][m]?
            vertices.append(0)
    return vertices

