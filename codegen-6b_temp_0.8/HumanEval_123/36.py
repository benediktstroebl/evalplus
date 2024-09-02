
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
    sequence = [n] + [collatz_helper(n, counter) for counter in range(1, 100)]
    return sorted(list(filter(lambda x: x % 2 != 0, sequence)))


assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(7) == [1, 7]
assert get_odd_collatz(8) == [1, 8]
assert get_odd_collatz(9) == [1, 9]
assert get_odd_collatz(10) == [1, 10]
assert get_odd_collatz(11) == [1, 11]
assert get_odd_collatz(12) == [1, 12]
assert get_odd_collatz(13) == [1, 13]
assert get_odd_collatz(14) == [1, 14]
assert get_odd_collatz(15) == [1, 15]
assert get_odd_collatz(16) == [1, 16]
assert get_odd_collatz(17) == [1, 17]
assert get_odd_collatz(18) == [1, 18]
assert get_odd_collatz(19) == [1, 19]
assert get_odd_collatz(20) == [1, 20]
assert get_odd_collatz(21) == [1, 21]
assert get_odd_collatz(22) == [1, 22]
assert get_odd_collatz(23) == [1, 23]
assert get_odd_collatz(24) == [1, 24]
assert get_odd_collatz(25) == [1, 25]
assert get_odd_collatz(26) == [1, 26]
assert get_odd_collatz(27) == [1, 27]
assert get_odd_collatz(28) == [1, 28]
assert get_odd_collatz(29) == [1, 29]
assert get_odd_collatz(30) == [1, 30]
assert get_odd_collatz(31) == [1, 31]
assert get_odd_coll