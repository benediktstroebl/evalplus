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

The `even_odd_palindrome` function iterates through all numbers between `1` and `n` and counts the numbers that are palindromes, distinguishing between even and odd palindromes and returning their counts as a tuple.

This solution should help you tackle the problem statement effectively, but if you'd like further clarification or have more questions, feel free to ask!