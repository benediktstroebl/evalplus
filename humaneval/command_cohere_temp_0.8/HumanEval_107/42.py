Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

This function iterates through numbers from 1 to `n` and determines whether each number is a palindrome. The `str` function is used to convert the integer `i` to a string `s` so that the reverse operation can be performed using the slice notation `s[::-1]`. If `s` matches its reverse, and the converted back integer value `int(s)` matches `int(s[::-1])`, then the number is considered a palindrome. The variable `len(s)` is used to check if the palindrome is even or odd length, updating the respective counts.

The script should operate correctly for the specified range of `n` values.  This approach does not require any additional libraries. It should provide a efficient solution in O(n) time complexity and is adaptable to the problem's constraints.