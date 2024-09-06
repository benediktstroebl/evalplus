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

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and checks if each number is a palindrome. 

For each palindrome, it increments the `even` counter if the number is even and the `odd` counter if the number is odd. Finally, it returns a tuple containing the counts of even and odd palindromes.

This approach provides a concise solution that meets the problem requirements.