Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_count = 0
        
        for j in range(1, len(reversed_str)+1):
            if reversed_str[:j] == reversed_str[::-1]:
                reversed_count += 1
        
        if reversed_count == 2:
            even_count += 1
        elif reversed_count == 1:
            odd_count += 1
    
    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple with two elements: the first element represents the count of even-length palindromes in the range `[1, n]`, and the second element represents the count of odd-length palindromes in the same range. The function iterates through all numbers between 1 and `n` and determines whether each number, when converted to a string, is a palindrome. It then counts the even and odd palindromes and returns the results as a tuple.