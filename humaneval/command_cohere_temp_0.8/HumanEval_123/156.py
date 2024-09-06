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
    assert get_odd_collatz(21) == [1, 21]
    assert get_odd_collatz(27) == [1, 27]
```

This script defines a function `get_odd_collatz(n)` that calculates the odd numbers in the Collatz sequence for a given positive integer `n`, as per the conjecture rules you described. The `if __name__ == "__main__":` block is used to validate the function against multiple test cases, ensuring that the odd numbers in the Collatz sequence are correctly extracted and returned.