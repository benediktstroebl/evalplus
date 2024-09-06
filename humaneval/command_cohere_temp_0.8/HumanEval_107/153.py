Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    s = str(n)
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == s[len(s)-1-i]:
            cnt += 1
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even += 1
        elif str(i) == str(i)[::-1] and i % 2 != 0:
            odd += 1
    return (even, odd)
```

Let's break down the code:
1. **Function Definition**:
   - `def even_odd_palindrome(n):`: This defines a function named `even_odd_palindrome` that takes a single argument `n`, which represents the upper limit of the range in which we want to count integer palindromes.
2. **String Conversion and Palindrome Counting**:
   - `s = str(n)`: Converts the integer `n` to a string.
   - `cnt = 0`: Initializes a counter `cnt` to zero to keep track of palindromes.
   - The loop `for i in range(len(s)-1):` iterates over each character of the string `s`.
   - `if s[i] == s[len(s)-1-i]:` checks if the characters at positions `i` and `len(s)-1-i` are the same. If they are, it means the character is part of a palindrome, and `cnt` is incremented.
3. **Even and Odd Classification**:
   - `even, odd = 0, 0`: Initializes two counters, `even` and `odd`, to keep track of even and odd palindromes, respectively.
   - The loop `for i in range(1, n+1):` iterates over each number from 1 to `n`.
   - `if str(i) == str(i)[::-1] and i % 2 == 0:` checks if `i` is a palindrome and if it's even. If both conditions are met, `even` is incremented.
   - `elif str(i) == str(i)[::-1] and i % 2 != 0:` checks if `i` is a palindrome and if it's odd. If both conditions are met, `odd` is incremented.
4. **Return Statement**:
   - The function returns a tuple `(even, odd)` containing the counts of even and odd palindromes, respectively.

This code efficiently calculates the number of even and odd palindromes within the range from 1 to `n` and returns the results as a tuple. It showcases a clear division of tasks: converting the input to a string, counting palindromes, and classifying them based on parity.