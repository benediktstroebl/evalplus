```python
def count_palindromes(n):
    # memoization for windowed palindrome count
    @cache
    def window_count(i, odd):
        if i > n:
            return 0, 0
        if i == n:
            return 1, 1 if odd else 1
        odd_count, even_count = window_count(i + 1, odd or i % 2 == 0)
        return even_count + odd_count, odd_count
    
    even, odd = window_count(1, 0)
    return even, odd

# Example usage
n = int(input())
even, odd = count_palindromes(n)
print(f"({}, {})".format(even, odd))
```

The key process is broken into a memoized windowed function `window_count` that calculates the count of odd and even palindromes within intervals `[1, n]`. Using recursion with memoization avoids redundant calculations, this improves efficiency significantly for larger `n`. The initial call is at `count_palindromes(n)`, which invokes `window_count(1, 0)` to process the interval `[1, n]`.