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

This function takes a positive integer `n` as input and returns a tuple containing two counts: the number of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome and the number is even, the even count is incremented; otherwise, the odd count is incremented. Note that this solution assumes integer inputs for palindromes and does not account for strings or other data types.