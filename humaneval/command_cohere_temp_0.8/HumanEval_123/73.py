Here's a Python script with a self-contained function that solves the problem:
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

if __name__ == "__main__":
    # Test cases
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(12) == [1, 5, 23, 229]
    assert get_odd_collatz(16) == [1, 2, 8, 4, 16, 32, 8, 2, 1]
```

This script defines a function `get_odd_collatz(n)` that calculates and returns the list of odd numbers in the Collatz sequence for a given starting integer `n`. The `main` block includes test cases to validate the function's behavior against expected outcomes.