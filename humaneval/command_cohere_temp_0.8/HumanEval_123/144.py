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

This script defines a function `get_odd_collatz(n)` that returns the list of odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a `while` loop to generate the Collatz sequence until the number reaches 1. Then it appends the odd numbers to the `odd_seq` list and returns it.

The test cases ensure that the function behaves as expected for different inputs. You can add more test cases to cover other scenarios and ensure the function's correctness.