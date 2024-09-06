Here's a Python script that contains a function named `even_odd_palindrome` designed to address the problem:
```python
def even_odd_palindrome(n):
    # Record the number of odd and even palindromes
    odd_count = 0
    even_count = 0
    
    # Range of integers to consider (inclusive of 1 and n)
    for num in range(1, n+1):
        # Check if the number is a palindrome
        if str(num) == str(num)[::-1]:
            # If the number is palindrome, check its parity
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return even_count, odd_count
```

This function accepts a positive integer `n` and returns a tuple that consists of the counts of even and odd integer palindromes within the range of 1 to `n` (inclusive).

The `str(num) == str(num)[::-1]` comparison checks if a number is a palindrome by comparing it to its reverse. The modulo operator (`%`) is used to determine if a palindrome is even or odd since an even number divided by 2 will have a remainder of 0, while an odd number divided by 2 will have a remainder of 1. 

You can incorporate the `even_odd_palindrome` function into your code, and it should work well provided that 1 <= n <= 10^3, as specified in the prompt.