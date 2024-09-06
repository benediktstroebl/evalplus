Here's a Python script that contains a function named `even_odd_palindrome` designed to address the problem:
```python
def even_odd_palindrome(n):
    # Initialize counters for even and odd palindromes
    even_count = 0
    odd_count = 0
    
    # Calculate the number of even and odd integer palindromes
    for num in range(1, n + 1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
```

This function accepts a positive integer `n` as input and produces a tuple that consists of the counts of even and odd integer palindromes within the range of 1 to `n` (inclusive). To determine if a number is a palindrome, it checks if the string representation of the number is equal to its reversed form. If it is, the function increments the appropriate counter based on whether the number is even or odd.

Feel free to test this function with various input values to verify its behavior. Let me know if you have any further questions or if you'd like to tackle more problems along these lines!