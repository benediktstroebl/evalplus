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

The `even_odd_palindrome` function iterates through all numbers between 1 and `n`, converting each number to a string and comparing it to its reverse (`str(i) == str(i)[::-1]`). If a number is a palindrome, the function checks if it's even or odd, updating the `even` or `odd` count accordingly. The function returns a tuple containing the counts for even and odd palindromes. 

This solution has a time complexity of `O(n)` as it iterates through `n` integers, and the space complexity is `O(1)` since it uses a constant amount of additional space.