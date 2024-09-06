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

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and determines whether each number is a palindrome. When it is, the variable `even` or `odd` is increased according to whether the number is even or odd. Ultimately, the function returns a tuple containing the count of even and odd integer palindromes. 

This approach follows the **brute-force** method, which involves checking if each integer is a palindrome by converting it to a string and comparing it to its reverse. Although it is simple, this method may not be the most efficient solution for larger values of `n`.