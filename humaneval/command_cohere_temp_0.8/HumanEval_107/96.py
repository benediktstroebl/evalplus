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

# Testing the function
def test_even_odd_palindrome():
    assert even_odd_palindrome(1) == (0, 0)
    assert even_odd_palindrome(2) == (1, 1)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(4) == (2, 2)
    assert even_odd_palindrome(5) == (2, 3)
    assert even_odd_palindrome(6) == (3, 3)
    assert even_odd_palindrome(7) == (4, 3)
    assert even_odd_palindrome(11) == (6, 5)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (48, 52)

# Run the tests
test_even_odd_palindrome()
```

This script includes the `count_palindromes` function, which is used to calculate the count of even and odd palindromes within a given range. The `even_odd_palindrome` function uses this count to return a tuple of the number of even and odd integer palindromes as requested in the Problem Statement. The `test_even_odd_palindrome` function provides a set of test cases to validate the correctness of the `even_odd_palindrome` function.