Here's a Python script that contains a function named `even_odd_palindrome` which takes in a positive integer `n` as an argument and returns a tuple with the count of odd and even palindromes in the range of 1 to `n` inclusive based on the given problem:
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

The `even_odd_palindrome` function calculates the number of even and odd-valued palindromes within the range of 1 to `n` (inclusive). It does so by iterating through each number between 1 and `n`, determining whether each number is a palindrome, and then incrementing the appropriate counter (`even` or `odd`) based on whether the number is divisible by 2 and therefore even, or odd. 

The script defines the function and handles the given Examples correctly.