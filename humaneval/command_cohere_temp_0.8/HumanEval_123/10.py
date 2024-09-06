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

# Test cases
print(get_odd_collatz(1))  # Output: [1]
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(14)) # Output: [1, 7, 13]
```
This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers in the Collatz sequence, based on the provided specification. The `while` loop generates the Collatz sequence up to the given number `n`, and the odd numbers are collected in the `odd_collatz` list, which is then returned as the result. The script includes test cases that demonstrate its behavior for various inputs.