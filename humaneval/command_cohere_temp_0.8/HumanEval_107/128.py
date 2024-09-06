Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 and `n` inclusive, in a markdown code block:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function calculates the number of even and odd-numbered palindromes within the range of 1 to `n` inclusively. It does so in a straightforward manner, counting the occurrences of even and odd-numbered palindromes through a loop. The final count is then returned in a tuple containing two elements, representing the numbers of even and odd-numbered palindromes, respectively.