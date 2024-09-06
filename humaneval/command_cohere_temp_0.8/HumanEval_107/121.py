```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function iterates through numbers from 1 to `n`, checking if each number is a palindrome by comparing its string representation with its reverse. If it is a palindrome, the `even` or `odd` count is incremented based on whether the number is even or odd. The function returns a tuple containing the counts of even and odd palindromes. 

This approach provides a straightforward solution that satisfies the problem requirements.