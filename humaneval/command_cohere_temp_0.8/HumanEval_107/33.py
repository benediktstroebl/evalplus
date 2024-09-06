Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def count_palindromes(n):
    even, odd = 0, 0
    for i in range(1, n+1):
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

In the script above, the `count_palindromes` function is used to iterate through numbers from 1 to `n` and keep track of the count of even and odd palindromes. The `even_odd_palindrome` function then calls this function and returns the results. Feel free to test this code with other input values to verify its correctness.  This code should pass the given tests since it's designed to solve the problem you provided.  If you encounter any difficulties or have more questions, please don't hesitate to ask!  The code includes tests to verify the correctness of the `even_odd_palindrome` function.