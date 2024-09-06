Here's a Python script that includes a self-contained function to solve the problem:
```python
def count_palindromes(n):
    # Count even palindromes
    even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
    # Count odd palindromes
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 != 0:
                odd += 1
    return even, odd

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    return count_palindromes(n)

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```

This script defines a function `even_odd_palindrome(n)` that takes a positive integer `n` as input and returns a tuple containing the count of even and odd integer palindromes within the range `[1, n]`. It employs two functions:
- `count_palindromes(n)`: This function computes the counts of even and odd palindromes and returns them as a tuple.
- `print(even_odd_palindrome(3))`: This function is a test case that calls the `even_odd_palindrome(n)` function with input `3` and prints the calculated result, which should be `(1, 2)` for the given example. 

When executed, the test case affirms the function's correctness. The output displays the expected count of even and odd palindromes, confirming the fulfillment of the problem statement's requirements.