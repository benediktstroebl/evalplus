```python
def count_palindromes(n):
    # count odd palindromes
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            odd += 1
    # count even palindromes
    even = 0
    for i in range(2, n+1):
        if str(i) == str(i)[::-1]:
            even += 1
    return even, odd
```

The `count_palindromes` function uses two loops to iterate through all numbers between 1 and `n` (inclusive) to count both even and odd palindromes. The `str(i)` conversion is used to ensure the value is treated as a string to easily compare it with its reverse. The loops increment a counter (`even` and `odd`) each time a number is a palindrome. The function returns the number of even and odd palindromes as a tuple.