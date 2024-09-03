def solution(lst):
    """Returns the sum of odd integers in even positions.

    Args:
        lst (list): A non-empty list of integers.

    Returns:
        int: Sum of odd elements in even positions.

    Examples:
        >>> solution([5, 8, 7, 1])
        12
        >>> solution([3, 3, 3, 3, 3])
        9
        >>> solution([30, 13, 24, 321])
        0
    """
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 != 0)