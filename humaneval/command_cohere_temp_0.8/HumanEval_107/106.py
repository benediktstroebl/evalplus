Here's a Python script that includes a self-contained function to solve the problem:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) == int(s[::-1]):
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```
This script defines the `even_odd_palindrome` function, which takes in a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range `[1, n]`.

The script employs a loop to iterate through numbers from 1 to `n`. For each number, it converts it to a string, checks if it's a palindrome, and determines if it's even or odd. Ultimately, it returns a tuple with the counts of even and odd palindromes.