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
    return (even, odd)

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```

In the script above, the `count_palindromes` function calculates the counts individually, and `even_odd_palindrome` uses this function to return the tuple of counts. Feel free to test it with other input values to verify its behavior. Let me know if you have any doubts or if you'd like to explore further enhancements or alternative approaches!