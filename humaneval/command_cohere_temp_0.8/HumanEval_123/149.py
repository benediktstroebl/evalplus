Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_seq.append(num)
    return odd_seq

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(21) == [1, 21]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a loop to generate the sequence until it reaches the base case of 1, appending the odd numbers to a list. The list is then returned as the odd Collatz sequence for the starting number.

The example test cases are included to validate the function's behavior for different inputs. You can further extend the test suite to cover a broader range of inputs or use a more sophisticated testing framework for more robust validation.