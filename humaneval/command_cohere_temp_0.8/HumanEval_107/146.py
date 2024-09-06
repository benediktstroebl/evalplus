```python
def count_palindromes(n):
    # memoization for counting even and odd length palindromes
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if len(str(i)) % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f'({even}, {odd})')
```

The `count_palindromes` function uses a recursive approach to count the number of palindromes within the range of `1` to `n`. It takes an integer `n` as input and returns a tuple of two counts, one for even-length palindromes and one for odd-length palindromes. The main function reads an integer `n` from the input, calculates the counts using the `count_palindromes` function, and prints the results as a tuple.