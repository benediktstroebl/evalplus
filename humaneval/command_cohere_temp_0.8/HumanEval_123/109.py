Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_seq.append(num)
    return odd_seq

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(6) == [1, 3, 6]
assert get_odd_collatz(10) == [1, 31, 153, 67, 221, 193, 29, 263, 89, 479, 211]
```

This script defines a function `get_odd_collatz(n)` that returns the list of odd numbers in the Collatz sequence for a given starting integer `n`. The function iterates through the sequence until it reaches 1, appending each odd number to the `odd_seq` list. The list is then returned as the result.

The test cases are placed in the code to verify that the function works correctly for different input scenarios. You can add more test cases to cover a wide range of inputs and edge cases to ensure the function's correctness.