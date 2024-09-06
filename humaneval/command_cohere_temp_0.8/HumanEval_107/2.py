Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1]:
            if len(s) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple containing the counts of even and odd-length palindromes within the range `[1, n]`. The test cases ensure that the function behaves as expected for various inputs. Adjust the variable `n` to change the range of interest.