Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = [3*i+1 for i in range(1, n+1, 2)]
    even_seq = [i/2 for i in range(n, 1, 2)]
    odd_seq.extend(even_seq)
    return odd_seq

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 16, 8, 4, 2, 1]
```
This approach first constructs the odd sequence until `n`, and then extends it with the even sequence from `n` down to 1. The final list is returned as the odd numbers in the Collatz sequence for the given input `n`.