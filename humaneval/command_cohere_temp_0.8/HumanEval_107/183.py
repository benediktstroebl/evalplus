Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 and `n`:
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

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it with its reverse. If the number is a palindrome and its parity (odd or even) is even, the `even` count is increased; otherwise, the `odd` count is increased. The function returns a tuple containing the even and odd counts.