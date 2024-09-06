Here's a Python script that includes a self-contained function to solve the problem:
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

The `count_palindromes` function is used to count the number of even and odd palindromes within a given range (`1`, `n`). It iterates through numbers from `1` to `n` and checks if each number is a palindrome. If it is, the function checks if the number is even or odd and increments the respective counter. 

The `even_odd_palindrome` function uses `count_palindromes` to compute the counts and returns the tuple of counts of even and odd palindromes.

Feel free to test this function with more input values to verify its correctness. Let me know if you have any other questions!