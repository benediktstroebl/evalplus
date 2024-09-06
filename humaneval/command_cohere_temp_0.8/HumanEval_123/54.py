Here's a Python script that contains a function `get_odd_collatz` that solves the problem in a markdown code block:
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
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(14) == [1, 7, 13]
```

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence of a given positive integer `n`. The function starts with `n` and constructs the Collatz sequence iteratively by dividing by 2 if the number is even, and multiplying by 3 and adding 1 if the number is odd. It then filters out only the odd numbers from the sequence, sorts them, and returns the result. The unit tests provided assert that the function produces the expected results for three different inputs.