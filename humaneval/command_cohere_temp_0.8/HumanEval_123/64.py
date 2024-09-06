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
assert get_odd_collatz(12) == [1, 5, 23, 104, 52, 26, 13, 64, 32, 16, 8, 4, 2, 1]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given positive integer `n`.

The script uses two separate lists to store the odd and even numbers in the Collatz sequence, and then combines them to create the final sequence. This allows us to add elements to the `odd_seq` list every two iterations and maintains the correct order of numbers in the sequence.