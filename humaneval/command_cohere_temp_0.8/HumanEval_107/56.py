Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range of 1 to `n`:
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

The `even_odd_palindrome` function uses two nested loops to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by comparing the string representation of the number with its reverse. If it's a palindrome and the number is even, the `even` counter is increased, and if it's odd, the `odd` counter is increased. Finally, the function returns a tuple of (even, odd) counts.