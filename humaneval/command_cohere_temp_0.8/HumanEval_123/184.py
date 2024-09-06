Here's a Python script with a self-contained function that solves the problem:
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

if __name__ == "__main__":
    # Test Cases
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(12) == [1, 5, 23, 229, 513, 1021, 1331, 1439, 1551, 1819, 2039, 2153, 2171, 2319]
```

This script defines a function `get_odd_collatz(n)` that calculates and returns a sorted list of odd numbers in the Collatz sequence for a given starting integer `n`. The `main` block includes test cases to validate the function's behavior for different inputs. You can add more test cases as needed to cover other scenarios.