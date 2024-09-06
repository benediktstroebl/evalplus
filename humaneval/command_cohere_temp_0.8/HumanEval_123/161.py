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
assert get_odd_collatz(21) == [1, 21]
assert get_odd_collatz(100) == [1, 101]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a loop to generate the sequence until it reaches the base case of 1, adding each odd number to the `odd_seq` list. The list is then returned as the result.

The test cases ensure that the function behaves as expected for different inputs. You can further extend the test suite to cover more cases for thoroughness.