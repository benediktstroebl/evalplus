Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 to `n`:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and int(s) % 2 != 0:
            odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to determine the counts of even and odd integer palindromes within the range of 1 to `n`. The function achieves this by iterating through numbers from 1 to `n` and checking if each number is a valid integer palindrome. If it is, the variable `even` is incremented if the number is even, and `odd` is incremented if the number is odd. Finally, the function returns a tuple containing the counts of even and odd integer palindromes. The output meets the requirements provided in the prompt, as it is a tuple with the number of even and odd integer palindromes, respectively.