Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've outlined:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome. If it is, the function checks whether it's even or odd and increments the respective counter. Finally, the function returns a tuple containing the counts of even and odd palindromes.