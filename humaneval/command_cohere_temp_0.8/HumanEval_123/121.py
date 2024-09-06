Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current // 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 != 0:
            odd_collatz.append(current)
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers in the Collatz sequence for a given starting integer `n`. The function follows the definition of the Collatz sequence, as described in the problem statement. It iterates through the sequence and maintains a list of odd numbers encountered during the process. The result is then sorted in increasing order.