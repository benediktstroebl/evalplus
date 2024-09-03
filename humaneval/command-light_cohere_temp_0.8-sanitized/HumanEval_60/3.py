def sum_to_n(n: int):
    """
    Sums all numbers from 1 up to n.
    Returns: number of digits in `n`
    """
    return ''.join(str(i) for i in range(1, n+1))