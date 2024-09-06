Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you have described:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) == int(s[::-1]):
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function uses two nested loops to iterate through all numbers from 1 to `n`. It converts each number to a string, checks if it's a palindrome, and increments the respective counter (`even` or `odd`) accordingly.

To test this function, you can run the following code, which would be for n = 12 as in your example:
```python
test_cases = [
    (3, (1, 2)),
    (12, (4, 6)),
    # Add more test cases as needed
    # ...
]

for n, expected in test_cases:
    print(f"Example {n}:")
    actual = even_odd_palindrome(n)
    print(f"Input: {n}")
    print(f"Output: {actual}")
    print(f"Explanation: {__doc__}")
    print("="*30)
```

This will provide an clear explanation of how the function works with illustrative tests. Feel free to add more tests to cover a range of scenarios.