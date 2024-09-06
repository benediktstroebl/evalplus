Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
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

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the count of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome and the number is even, the `even` count is incremented; otherwise, the `odd` count is incremented. Finally, the function returns a tuple of (even, odd). 

This solution has a time complexity of `O(n)` since it iterates through each number from 1 to `n` once, which makes it efficient for the given constraints.