from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    def _rolling_max(i: int, x: int) -> Tuple[int, List[int]]:
        """Rolling max algorithm. Recursive function that makes use of memoization.

        Parameters
        ----------
        i : int
            current index in the sequence
        x : int
            current element in the sequence

        Returns
        -------
        Tuple[int, List[int]]
            max element found so far and a list of all the elements until now that are the max
        """

        if i == 0:
            return x, [x]
        if i == 1:
            return max(x, numbers[i-1]), [max(x, numbers[i-1])]
        memo = memoization(i)
        if memo is None:
            max_value, max_list = _rolling_max(i-1, numbers[i-1])
            max_value, max_list = max(max_value, x), [x] if max_value == x else max_list + [x]
            memo = (max_value, max_list
