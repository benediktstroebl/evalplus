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

The function initializes two counters, `even` and `odd`, to 0. It then iterates through the range from 1 to `n` (inclusive), where for each integer `i`, it checks if `i` is a palindrome by comparing its string representation with its reverse (`str(i) == str(i)[::-1]`). If it is a palindrome, the function checks if it's even or odd, and increments the respective counter accordingly.

Finally, the function returns a tuple containing the two counters, representing the number of even and odd integer palindromes in the specified range.