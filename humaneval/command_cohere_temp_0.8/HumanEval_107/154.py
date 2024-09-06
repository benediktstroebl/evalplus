Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range(1, n+1), inclusive:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and int(s) % 2 != 0:
            odd += 1
    return (even, odd)
```

The function leverages modular arithmetic and string manipulation to efficiently determine the counts of even and odd integer palindromes. The returned tuple provides the respective counts of even and odd palindromes within the specified range.