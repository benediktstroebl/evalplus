Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Generate all integer palindromes from 1 to n
    pmns = [str(i) for i in range(1, n+1) if i == int(i)[::-1]]
    even_count = len(pmns) // 2
    odd_count = len(pmns) - even_count
    return even_count, odd_count
```

This script defines a function `even_odd_palindrome(n)` that takes a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes in the range `[1, n]`.

The `pmns` list computes all the integer palindromes from 1 to `n` and stores them as strings in the list. Then, it calculates the length of this list which is evenly divided by 2 to get the even count, and the difference between the length and even count gives the odd count.

The given code is self-contained and should work correctly for the described problem. You can use it as a solution to the problem you posted.