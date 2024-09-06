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

# Tests
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(21) == [1, 21]
```

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given starting integer `n`. The function iterates through the sequence until it reaches 1, collecting odd numbers along the way, and returns them in reverse order, which is why we reverse the list afterwards. The initial test cases are included as well to validate the function.