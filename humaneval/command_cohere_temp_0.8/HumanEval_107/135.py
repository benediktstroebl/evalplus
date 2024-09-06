```python
def count_palindromes(n):
    # Count even and odd length palindromes
    even, odd = 0, 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and len(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and len(s) % 2:
            odd += 1
    
    return even, odd

n = int(input())
even, odd = count_palindromes(n)
print(f"(#{even}, #{odd})")
```

The `count_palindromes` function takes a positive integer `n` as input and aims to determine the number of even and odd-length palindromes within the range `[1, n]`. It iterates through each number from 1 to `n` and checks whether its string representation, `s`, is a palindrome. If it is, the variable `even` or `odd` is incremented based on whether the length of `s` is even or odd. The result is then returned as a tuple.