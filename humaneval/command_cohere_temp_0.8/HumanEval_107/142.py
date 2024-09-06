Here's a Python script that includes a function to solve the problem:
```python
def count_palindromes(n):
    s = str(n)
    ev = se = 0
    for e in s:
        if e == e[::-1]:
            ev += 1
        else:
            se += 1
    return ev, se

def even_odd_palindrome(n):
    return count_palindromes(n)
```

The `count_palindromes` function converts a number to a string, then iterates through each character, counting occurrences of palindromes. The `even_odd_palindrome` function uses this function to count the number of even and odd palindromes within the range `[1, n]`.