Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
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

This function takes a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range `[1, n]`. The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by comparing its string representation with its reverse. If it's a palindrome and the number is even, it adds 1 to the `even` count; otherwise, it adds 1 to the `odd` count. The function then returns a tuple of (even, odd) counts.