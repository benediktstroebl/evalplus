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

This function takes in a positive integer `n` as input and aims to determine the count of even and odd integer palindromes within the range `[1, n]`. It achieves this by iterating through the numbers from 1 to `n` and checking if each number is a palindrome. If it is, the count is incremented accordingly based on whether the number is even or odd. The function finally returns a tuple containing the counts of even and odd palindromes. 

The unit tests for this function are omitted, as per your instructions, however, they are minimal and should be implemented to ensure the function's correctness.