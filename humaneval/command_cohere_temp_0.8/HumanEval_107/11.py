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

This function iterates through numbers from 1 to `n` and checks if each number is a palindrome. The `str` function converts the integer `i` to a string `s`, and `s[::-1]` reverses the string. If the original integer and its reverse are equal, and the length of `s` is even, then it is considered an even palindrome; otherwise, it is considered an odd palindrome. The function counts the number of even and odd palindromes and returns them as a tuple.