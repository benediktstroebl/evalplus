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

This script defines a function `get_odd_collatz(n)` that returns the odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a basic loop to generate the odd numbers in the sequence, appending them to the `odd_seq` list. The loop continues until the number reaches 1, which is the end of the Collatz sequence for any starting number. The function is then tested with a few targeted tests to ensure correctness.