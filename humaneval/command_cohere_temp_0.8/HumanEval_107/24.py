Here's a Python script that includes a self-contained function to solve the problem:
```python
def even_odd_palindrome(n):
    # collect all positive integer palindromes and categorize them based on parity
    counts = collections.Counter(str(i) for i in range(1, n+1) if i == int(str(i)[::-1]))
    even, odd = 0, 0
    for num in counts:
        if counts[num] % 2 == 0:
            even += counts[num]
        else:
            odd += counts[num]
    return (even, odd)
```

This function uses a dictionary comprehension to generate a Counter object, which counts the number of palindromes within the range(1, n). The Counter object is then queried to retrieve the counts of even and odd palindromes, which are returned as a tuple. This solution is efficient and easily extensible for larger test cases.