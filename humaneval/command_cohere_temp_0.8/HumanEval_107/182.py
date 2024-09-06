Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_count = 0
        
        for j in range(len(reversed_str)):
            if reversed_str[j] == reversed_str[0]:
                reversed_count += 1
            else:
                break
        
        if reversed_count == len(reversed_str) or reversed_count == len(reversed_str)/2:
            if reversed_count == len(reversed_str):
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)
```

This script provides a function that takes in a number `n` as input, counts the number of even and odd length palindromes within the range of `1` to `n` (inclusive), and returns a tuple containing those two counts.

The `str(i)` conversion is used to convert the integer `i` to a string for the palindrome check. The loop iterates through each digit of the string and counts the number of matching digits at the start and end of the string to determine if it's a palindrome. The count is incremented based on whether it is a full palindrome or a half palindrome. 

The script returns a tuple with the counts of even and odd palindromes.