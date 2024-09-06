Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 and `n`:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and counts the numbers that are palindromes. For each palindrome number, the function checks if it's even or odd and increments the respective counter. Finally, the function returns a tuple containing the counts of even and odd palindrome numbers. 

This approach provides an efficient solution that linearly traverses the numbers and applies a few string manipulations to check for palindromes. The result is a clear and concise Python function that solves the problem statement in a self-contained manner.