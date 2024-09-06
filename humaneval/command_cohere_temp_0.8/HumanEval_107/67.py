Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def counting_palindromes(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even, odd = counting_palindromes(n)
    return even, odd

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```

In the function `even_odd_palindrome`, we call the helper function `counting_palindromes` to calculate the counts of even and odd palindromes. The `counting_palindromes` function iterates through numbers from 1 to `n` and keeps track of the counts by checking if a number is a palindrome and whether it's even or odd. The final counts are returned as a tuple, which is then used to return the result from the `even_odd_palindrome` function.