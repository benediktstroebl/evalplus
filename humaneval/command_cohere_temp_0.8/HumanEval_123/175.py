Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] > 1: 
            sequence.extend([sequence[-1] // 2, sequence[-1] * 3 + 1])
        sequence.pop()
    odd_collatz.sort()
    return odd_collatz

# Tests
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```
This script defines a function called `get_odd_collatz(n)` that takes a positive integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence. The function uses an iterative approach to construct the Collatz sequence and selects only the odd numbers, finally sorting them.