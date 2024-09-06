Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    s = str(n)
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == s[len(s)-1-i]:
            cnt += 1
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
        elif str(i) == str(i)[::-1] and i % 2 != 0:
            odd += 1
    return (even, odd)
```

This function takes a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range from 1 to `n` (inclusive). It iterates through each digit in the decimal representation of `n`, and if it finds a matching digit at the opposite end of the number (indicative of a palindrome), it increments the `cnt` variable. Afterward, it separately counts even and odd palindromes within the range from 1 to `n` and returns the counts as a tuple.