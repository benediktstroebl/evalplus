Here's a Python script that includes a function to solve the given problem:
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
This script defines the `even_odd_palindrome` function, which takes in a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range `[1, n]`. The function uses two loops to iterate through all numbers between 1 and `n`. It converts each number to a string and checks if it's a palindrome and an integer. If it is, the function increments the appropriate counter (`even` or `odd`), which is returned at the end.