```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function iterates through all numbers between `1` and `n` and counts the numbers that are palindromes, recognizing whether they are even or odd. The result is a tuple containing the count of even and odd-ending palindromes. This solution is efficient and straightforward, providing the required counts of even and odd palindromes within the given range. It ensures that the counts are correctly tallied based on whether the palindrome is even or odd.