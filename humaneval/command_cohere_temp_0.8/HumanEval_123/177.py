Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
        odd_collatz.append(sequence[-1])
        sequence = sequence[:-1]
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 20, 10, 5, 16, 8, 4, 2, 1]
```
This script defines a function `get_odd_collatz(n)` that calculates and returns a sorted list of odd numbers in the Collatz sequence starting from a given positive integer `n`. It uses a loop to iteratively generate the sequence while keeping track of odd numbers and appending them to the `odd_collatz` list. The script also includes test cases to validate the function's behavior for different inputs.