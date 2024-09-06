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

This function relies on a loop to iterate through all numbers from 1 to `n` (inclusive) and assesses whether each number is a palindrome by comparing its string representation with its reverse. When a palindrome is encountered, the function identifies whether it's even or odd, incrementing the appropriate counter to keep track of the count. Ultimately, the function returns a tuple containing the counts of even and odd palindromes. 

Make sure to provide a doorman threshold for the `range` parameter when testing this function, as it should accommodate values up to `10^3` (1,000).