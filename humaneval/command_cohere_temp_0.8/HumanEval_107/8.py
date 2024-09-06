Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        reversed_num = str(num)
        if reversed_num == reversed_num[::-1] and int(reversed_num) == num:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function `even_odd_palindrome(n)` calculates the number of even and odd integer palindromes within the range `[1, n]`. It uses two variables, `even` and `odd`, to keep track of the count of even and odd palindromes, respectively.

You can call this function with any integer input `n` to obtain the count of even and odd palindromes within the specified range.