```python
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    Collatz conjecture is
    is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term obtained from
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5
    """
    if n < 1:
        return []
    if n % 2 == 0:
        return [n]
    a = get_odd_collatz(n // 2)
    b = a[::-1]
    return [3 * a[i] + i for i in range(1, len(a))]
```

This code defines a function called `get_odd_collatz()` that takes a positive integer `n` as input and returns a list of the odd numbers in the Collatz sequence for `n`. This sequence is defined using the Collatz conjecture, which states that for any positive integer `n`, the sequence of numbers will always reach 1. The function first checks if `n` is less than 1, and if so, returns an empty list. If `n` is an positive number, the function proceeds to calculate the odd numbers in the Collatz sequence for `n` using recursion. 

The function calls itself with `n//2` to calculate the odd numbers in the sequence, and then uses list slicing to reverse the order of the odd numbers and create a list of odd numbers. The function then uses list comprehension to create a list of `3` multiplied by each odd number `i` (starting from `i = 1`) plus `i`, where `i` is the index of each element in the list.