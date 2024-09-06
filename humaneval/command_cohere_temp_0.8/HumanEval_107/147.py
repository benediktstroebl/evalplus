Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
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

The function takes a positive integer `n` as input and returns a tuple containing two counts: the number of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The `str(i) == str(i)[::-1]` checks if a number is a palindrome by comparing the string representation of the number with its reverse. The `i % 2 == 0` checks if the palindrome is even.

The script can be tested with the following inputs to verify that it correctly calculates the number of even and odd palindromes:
```python
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
``` 

This script will provide the number of even and odd-integer palindromes for any positive integer input within the specified range. Note that the provided code is a simple linear sweep from 1 to n, which is efficient enough for this problem considering the specified limit of `10^3`.