Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the number of even and odd integer palindromes, respectively, that fall within the range from 1 to `n` (inclusive). 

The `for` loop goes through each integer from 1 to `n` and checks whether its decimal representation is the same when reading forward and backward (i.e., it checks if the integer is a palindrome). If it is a palindrome, then it checks whether it's even or odd, and increments the respective counter. Finally, the function returns a tuple containing both counters.