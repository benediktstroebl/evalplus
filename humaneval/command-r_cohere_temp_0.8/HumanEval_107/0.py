```python
def even_odd_palindrome(n):
    """
    Count the number of even and odd integer palindromes between 1 and n inclusive.

    Parameters:
        n (int): Upper limit of the range.

    Returns:
        tuple: A tuple containing the count of even and odd integer palindromes.
    """
    even, odd = 0, 0

    # Palindrome with a single digit
    for i in range(1, n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    # Palindrome with two digits
    for i in range(10, n + 1):
        temp = i
        reversed_i = 0
        while temp > 0:
            reversed_i = reversed_i * 10 + temp % 10
            temp //= 10
        if i == reversed_i:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    return (even, odd)
```