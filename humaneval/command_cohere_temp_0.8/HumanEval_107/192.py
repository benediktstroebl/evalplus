Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range from 1 to `n` (inclusive):
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function iterates through the range from 1 to `n` and checks if each `int` is a palindrome by converting it to a `str` and comparing it with its reverse. If the number is a palindrome and is even, it adds 1 to the `even` count, else it adds 1 to the `odd` count. The function finally returns a tuple containing the even and odd counts.