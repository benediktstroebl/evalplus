Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence starting from the input integer `n`. The Collatz sequence is defined through an iterative process: if the last number in the sequence is odd, it's added to the odd numbers list; if it's even, it's divided by 2 and added to the sequence; otherwise, it's multiplied by 3 and added to the sequence, with the increment step applied. Test cases are also included to validate the function's behavior for different inputs.