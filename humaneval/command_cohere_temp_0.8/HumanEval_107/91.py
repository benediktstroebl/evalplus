Here's a Python script that contains a function named `even_odd_palindrome` designed to address the problem:
```python
def even_odd_palindrome(n):
    # Record the number of odd and even palindromes
    odd_count = 0
    even_count = 0
    
    # Iterate through the range from 1 to n
    for num in range(1, n+1):
        # If the number is a palindrome and odd, increment the odd count
        if str(num) == str(num)[::-1] and num % 2 != 0:
            odd_count += 1
        # If the number is a palindrome and even, increment the even count
        elif str(num) == str(num)[::-1] and num % 2 == 0:
            even_count += 1

    # Return the recorded counts as a tuple
    return (even_count, odd_count)
```

This function accepts a positive integer `n` and returns a tuple that consists of the counts of even and odd integer palindromes within the range of 1 to `n` (inclusive). It achieves this by iterating through the range and applying checks for palindromes and even/oddness.

Remember to ensure that `n` is within the specified range (1 to 10^3) for the function to operate correctly.