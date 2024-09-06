Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) == int(s[::-1]):
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to calculate the count of even and odd integer palindromes within the range of 1 to `n` (inclusive). The function first initializes two counters, `even` and `odd`, to zero. It then iterates through the numbers from 1 to `n` using a `for` loop. For each number `i`, it converts it to a string `s` and checks if the string `s` is a palindrome and if the reversed string `s[::-1]` produces the same integer when converted to an integer. If both conditions are met, the function checks if the length of the string `s` is even, it increments the `even` counter; otherwise, it increments the `odd` counter. Finally, the function returns a tuple containing the counts of even and odd integer palindromes.