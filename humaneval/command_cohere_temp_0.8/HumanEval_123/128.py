Here's a Python script with a self-contained function that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current / 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 == 1:
            odd_collatz.append(current)
    odd_collatz.sort()
    return odd_collatz
```

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence for a given positive integer `n`. The function starts with `n` and iteratively applies the Collatz sequence recursively to construct the sequence. It tracks odd numbers during this process and finally sorts these odd numbers to return the result.

This implementation has a time complexity of `O(2^n)` because the Collatz sequence doubles in size with each iteration, which corresponds to the recursive structure of the algorithm. It uses a maximum of one disk's worth of memory (32-bit or 64-bit depending on your system) due to the iterative list comprehension that grows the sequence.