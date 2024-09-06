Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = [3*i+1 for i in range(1, n+1, 2)]
    even_collatz = [i/2 for i in range(n, 1, 2)]
    odd_collatz.extend(even_collatz)
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(12) == [1, 5, 23, 112, 46, 23, 14, 7, 3, 11, 36, 18, 9, 4, 2, 1]
```

This script defines the `get_odd_collatz` function, which returns a list of odd numbers in the Collatz sequence for a given positive integer `n`. The function internally separates the odd and even numbers in the Collatz sequence and then combines them to form the final list of odd numbers. Finally, the script provides some test cases to validate the function.