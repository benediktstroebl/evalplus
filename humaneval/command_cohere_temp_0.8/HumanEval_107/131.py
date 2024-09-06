Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
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

This function takes in a positive integer `n` as input and aims to return a tuple containing the counts of even and odd integer palindromes in the range `[1, n]`. The function uses a loop to iterate through all numbers between 1 and `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome and its length is evenly divisible by 2, it is counted as even; otherwise, it is counted as odd. The counts are accumulated and returned as a tuple.