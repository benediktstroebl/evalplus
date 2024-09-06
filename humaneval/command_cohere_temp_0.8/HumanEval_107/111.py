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

The function employs a simple loop to iterate through all numbers between 1 and `n` (inclusive), and for each number, it checks if it is a palindrome by comparing its string representation with its reverse. If it is a palindrome and the number is even, the `even` count is increased; otherwise, the `odd` count is increased. Finally, the function returns a tuple of (even, odd) counts.