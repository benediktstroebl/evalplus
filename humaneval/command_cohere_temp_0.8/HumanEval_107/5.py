Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 to `n`:
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

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and counts the numbers that are palindromes. If the palindrome is even, it adds to the `even` count, and if it's odd, it adds to the `odd` count. The function returns a tuple of these two counts. 

This solution is efficient and directly addresses the prompt's request, producing the correct counts of even and odd-palindromes up to 10,000.