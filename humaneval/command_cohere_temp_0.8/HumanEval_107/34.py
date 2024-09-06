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

The function takes a positive integer `n` as input and returns a tuple containing the count of even and odd integer palindromes within the range of 1 to `n` (inclusive). It iterates through each digit in the decimal representation of `n`, and if it finds a matching digit at the same position in reverse, it increments the `cnt` counter. Afterward, it individually counts even and odd palindromes by iterating through the range from 1 to `n` and checking if each number is a palindrome and whether it's even or odd, updating the respective counts. The final count is returned as a tuple of two values, representing the count of even and odd integer palindromes.