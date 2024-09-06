Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Create a reversible string
        reversible = str(i)
        reversed_reversible = reversible[::-1]
        
        if reversible == reversed_reversible:
            if len(reversible) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)
```

This function takes a single parameter `n`, which represents the upper limit for generating palindromes. It uses a `for` loop to iterate through numbers from 1 to `n`, and for each number, it creates a reversible string, which is then reversed and compared to the original to check if it's a palindrome. If it is, the length of the reversible string is checked to determine if it's even or odd, and the appropriate counter is increased.

The function returns a tuple containing two values: the number of even-length palindromes and the number of odd-length palindromes within the range `[1, n]`.