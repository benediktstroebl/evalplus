Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_str = reversed_str[::-1]
        if int(reversed_str) == i: 
            if len(reversed_str) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
```

This function takes in a number `n` as input and returns a tuple containing two integers representing the count of even and odd palindromes within the range `[1, n]`. The code iterates through each number between 1 and `n` and determines whether it is a palindrome. If it is, then it checks whether the length of the palindrome is even or odd and increments the appropriate count variable. Finally, the function returns a tuple of `(even_count, odd_count)` respectively.