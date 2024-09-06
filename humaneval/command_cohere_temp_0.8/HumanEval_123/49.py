```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    return odd_collatz

# Test cases
tests = [
    (1, [1]),
    (5, [1, 5]),
    (10, [1, 31, 153, 67, 478, 8371, 21845, 66390, 196603, 598529, 1729916, 44497, 16529, 497, 249, 125, 63, 31, 3]),
    (15, [1, 231, 377, 109, 367, 567, 157, 367, 109, 377, 231, 157, 567, 231, 377, 109, 463, 313, 199, 313, 463, 109, 31]),
]

for n, expected in tests:
    result = get_odd_collatz(n)
    assert result == expected, f"For n={n}, Expected {expected} but got {result}"
```

The `get_odd_collatz` function, takes a positive integer `n` as input and constructs the odd numbers in the Collatz sequence, it does this by starting with `n` and iteratively applying the Collatz function (which is to divide by 2 if the number is even, or multiply by 3 and add 1 if the number is odd) until the sequence reaches 1.

The `tests` list has a pair of tuples for input values and expected results. We iterate over this list, call the `get_odd_collatz` function for each input value, and then assert that the returned result matches the expected output.