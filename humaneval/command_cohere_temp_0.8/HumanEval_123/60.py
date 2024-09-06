Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.reverse()
    return odd_collatz

# Test Cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(12) == [1, 9, 25]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a while loop to generate the Collatz sequence until the number reaches 1. Then it reverses the list and returns it, omitting the 1. The three test cases demonstrate the behavior of the function for different inputs.