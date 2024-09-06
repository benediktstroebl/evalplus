Here's a Python script that contains a function named `even_odd_palindrome` designed to address the given problem:
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

The function `even_odd_palindrome(n)` employs a loop to traverse integers from 1 to `n` (inclusive). When an integer is encountered that forms a palindrome when read forwards and backwards, the function examines its parity (even or odd) and increments the appropriate counter. Ultimately, the function returns a tuple containing the counts of even and odd palindromes.