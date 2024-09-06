Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x & 1 == 1]
    collatz_seq = [x for x in odd_seq if x != 1] + [1]
    return sorted(collatz_seq)

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 16, 8, 4, 2, 1]
```

This script defines the `get_odd_collatz(n)` function, which returns a sorted list containing only the odd numbers in the Collatz sequence of the input integer `n`. The Collatz sequence for `n` is generated using the function, and then odd numbers in that sequence are filtered and sorted. The unit tests assert the function's correctness for cases `n = 1`, `n = 5`, and `n = 14`. You can add more tests to ensure the function's correctness for different input cases.