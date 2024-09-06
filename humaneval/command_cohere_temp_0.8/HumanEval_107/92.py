Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to calculate the count of even and odd integer palindromes within the range from 1 to `n` (inclusive). The function iterates through the numbers from 1 to `n`, converts each number to a string, and checks if it's a palindrome by comparing it to its reverse (`str(num) == str(num)[::-1]`). If it's a palindrome, it increments the respective count (`even` or `odd`) based on whether the number is even or odd. Finally, the function returns a tuple containing the counts of even and odd palindromes.