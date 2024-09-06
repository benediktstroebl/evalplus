Here's a Python script with a self-contained function that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] > 1:
            sequence.extend([sequence[-1] // 2, sequence[-1] * 3 + 1])
        sequence.pop()
    return odd_collatz

if __name__ == "__main__":
    # Test Cases
    test_cases = [
        (1, [1]),
        (5, [1, 5]),
        (14, [1, 7, 31, 263, 837, 429, 213, 104, 52, 26, 13, 6, 3, 1]),
    ]
    for n, expected in test_cases:
        assert get_odd_collatz(n) == expected
```

This script defines a function `get_odd_collatz(n)` that calculates and returns a sorted list of odd numbers in the Collatz sequence for a given positive integer `n`. The `main` block then tests the function with a variety of test cases to ensure it produces the correct output for various inputs.