Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def count_palindromes(n):
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
    even, odd = count_palindromes(n)
    return even, odd

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```

In the `count_palindromes` function, we iterate through numbers from `1` to `n` and keep track of even and odd palindromes using the `even` and `odd` variables. In the `even_odd_palindrome` function, we call `count_palindromes` and return the result as a tuple. The script includes test cases to verify the function's behavior for different input values.