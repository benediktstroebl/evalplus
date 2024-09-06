Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

This function iterates through numbers from 1 to `n` and checks if each number is a palindrome. The `even` and `odd` counters are incremented accordingly based on whether the length of the numeric palindrome is even or odd. The function finally returns a tuple containing the counts of even and odd palindromes. 

Make sure to test this code with a appropriate testing framework to ensure its correctness.