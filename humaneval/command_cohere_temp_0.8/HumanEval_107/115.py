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

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the count of even and odd integer palindromes within the range `[1, n]`. The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If it's a palindrome and the number is even, it increments the even count; otherwise, it increments the odd count. The function returns a tuple with these two counts.