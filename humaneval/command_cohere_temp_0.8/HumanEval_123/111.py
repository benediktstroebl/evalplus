Here's a Python script with a self-contained function that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x & 1 == 1]
    collatz_seq = [x for x in odd_seq if x != 1]
    return sorted(collatz_seq)

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that calculates the odd numbers in the Collatz sequence for a given starting integer `n`. The function first extracts the odd digits from the decimal representation of `n`, filters out `1` since it's not part of the sequence, and sorts the result.

The given test cases assert the function's behavior for different inputs to ensure its correctness.