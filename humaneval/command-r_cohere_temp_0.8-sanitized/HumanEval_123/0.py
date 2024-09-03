def get_odd_collatz(n):
    """
    Returns a sorted list of odd numbers in the Collatz sequence.

    Args:
        n (int): A positive integer.

    Returns:
        list: A sorted list containing odd numbers in the Collatz sequence.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            sequence.append(n)
    sequence.sort()
    return sequence