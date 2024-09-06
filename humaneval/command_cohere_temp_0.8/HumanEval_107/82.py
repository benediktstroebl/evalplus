Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Calculate the maximum number of palindromes
    max_palindromes = n * (n + 1) // 2

    # Count even and odd palindromes
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range `[1, n]`. It first calculates the maximum possible number of palindromes (using the formula `n * (n + 1) // 2` for `max_palindromes`) and then counts the occurrence of each kind of palindrome, updating the `even_count` and `odd_count` accordingly.