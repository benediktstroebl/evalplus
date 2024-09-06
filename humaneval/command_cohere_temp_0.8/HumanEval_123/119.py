Here's a Python script with a self-contained function that solves the problem:
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
        sequence = sequence[1:]
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(12) == [1, 7, 5, 12]
assert get_odd_collatz(14) == [1, 7, 19, 5, 2, 14]
```
This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers in the Collatz sequence, starting from a given positive integer `n`. The function initializes an empty list `odd_collatz` and an initializes a sequence with `n` as the first element. It then enters a loop where it evaluates the next step in the Collatz sequence and appends the odd numbers to the `odd_collatz` list. Finally, the function returns the `odd_collatz` list.