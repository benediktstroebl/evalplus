Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    s = str(n)
    cnt = 0
    for i in range(len(s)//2):
        if s[:i] == s[i::]:
            cnt += 1
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i%2 == 1:
            odd += 1
        if str(i) == str(i)[::-1] and i%2 == 0:
            even += 1
    return (even, odd)
```

This function takes a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range from 1 to `n` (inclusive). It iterates through the digits of `n` to count all possible palindromic integers within the range, and then separately counts the even and odd ones based on the parity of the palindromic integer. The output of the function follows the format of the given examples, where the tuple contains the counts of even and odd integer palindromes, respectively.