```python
def count_palindromes(n):
    # memoization for counting even and odd length palindromes
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            even += 1
        else:
            odd += 1
    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f"(?, {})".format(even, odd))
```

The `count_palindromes` function uses two variables to count the even and odd-length palindromes in the range from 1 to `n` (`even, odd = 0, 0`). It iterates through the range and checks if each number `i` is a palindrome by comparing its string representation to its reversed version. If it is a palindrome, the corresponding counter is incremented (`even += 1` or `odd += 1`). The final result is returned as a tuple.