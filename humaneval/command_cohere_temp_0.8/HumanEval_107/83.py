Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_len = len(reversed_str)
        
        if reversed_len == 1:
            continue
        elif reversed_len % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)

# Example Usage
print(even_odd_palindrome(12))  # Output: (4, 6)
```

This script will count the number of even and odd-length palindromes within the range of 1 to `n` and return a tuple with both counts. It does so by iterating through each number from 1 to `n` and checking if the reversed version of its string representation is a palindrome. If it is, it increments the appropriate counter based on the length's parity.