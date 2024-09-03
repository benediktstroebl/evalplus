```python
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    Collatz conjecture is
    is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term obtained from 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing.

    Returns: get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    return [odd_list(n)]

def odd_list(n):
    """
    Generate the list of odd numbers in collatz sequence for n.
    """
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n]
    else:
        return [2 * n + 1] + odd_list(n // 2)

# Example usage:
print(get_odd_collatz(5))  # [1, 5]
```
This script defines a function `get_odd_collatz` that generates a list of the odd numbers in the Collatz sequence for a given positive integer `n`. The `odd_list` function generates the list of odd numbers by checking the current number's parity, and recursively calling itself with the parity of the square root of the current number.