Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_str = reversed_str[::-1]
        if reversed_str == str(i):
            if len(str(i)) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple containing two integers representing the counts of even and odd-length palindromes within the range `[1, n]`. The code iterates through numbers from `1` to `n` and determines whether each number is a palindrome. If it is, the function checks whether the length of the number is even or odd and increments the respective count variable.

The output of this function will be a tuple (even_count, odd_count) that indicates the number of even and odd-length palindromes within the specified range.