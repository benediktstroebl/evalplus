Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Counter for even and odd palindromes
    even, odd = 0, 0
    
    # Range to iterate through numbers up to n
    for num in range(1, n+1):
        # If the number is a palindrome and is even
        if str(num) == str(num)[::-1] and num % 2 == 0:
            even += 1
        # If the number is a palindrome and is odd
        elif str(num) == str(num)[::-1] and num % 2 != 0:
            odd += 1
    
    return (even, odd)
```

This function takes a positive integer `n` as input and returns a tuple containing two integers representing the number of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The function uses two counters, `even` and `odd`, to keep track of the number of even and odd palindromes, respectively. It then iterates through numbers from 1 to `n` and checks if a number is a palindrome and whether it is even or odd, incrementing the corresponding counter accordingly. Finally, the function returns a tuple of the two counters.