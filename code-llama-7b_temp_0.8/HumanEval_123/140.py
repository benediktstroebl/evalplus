
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """

    """
    # Note: The list comprehension version is 10 times faster than the recursive version.
    def collatz_sequence(n):
        if n == 1:
            return [1]
        elif n % 2 == 0:
            return collatz_sequence(n / 2) + [n / 2]
        else:
            return collatz_sequence(3 * n + 1) + [3 * n + 1]

    return sorted(i for i in collatz_sequence(n) if i % 2 != 0)
    """

    def collatz_sequence(n):
        # A list of odd integers in the collatz sequence for n.
        collatz = []
        while n > 1:
            if n % 2 != 0:
                collatz.append(n)
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
        if n == 1:
            collatz.append(1)
        return collatz

    # the odd numbers in collatz sequence of n.
    return sorted(i for i in collatz_sequence(n))

