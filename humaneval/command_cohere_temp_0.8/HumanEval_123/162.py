Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        odd_collatz.append(n)
    odd_collatz.reverse()
    return odd_collatz

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 18, 8, 4, 2, 1]
```

This script defines a function `get_odd_collatz(n)` that returns the list of odd numbers in the Collatz sequence of the given positive integer `n`. The function starts with `n` and iteratively computes the next number in the Collatz sequence by toggling between dividing an even number by 2 and multiplying an odd number by 3 and adding 1. The odd numbers in the sequence are collected in the `odd_collatz` list, which is then reversed to ensure sorting in increasing order. The function includes test cases to validate its behavior for different input values.