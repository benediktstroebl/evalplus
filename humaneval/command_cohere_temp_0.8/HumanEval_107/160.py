Here's a Python script that includes a function to solve the given problem:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and int(s) % 2 != 0:
            odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function iterates through all numbers between `1` and `n`, converts them to strings, and checks if they are palindromes. If they are palindromes and their corresponding number is even, then the `even` counter is increased; otherwise, the `odd` counter is increased. Finally, the function returns a tuple containing the counts for even and odd palindromes. 

This solution should be able to pass any test cases for the provided problem statement. Feel free to ask any more questions or request further assistance!