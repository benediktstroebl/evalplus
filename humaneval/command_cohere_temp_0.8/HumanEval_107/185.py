Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range of 1 and `n` inclusive:
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

The function counts the even and odd integer palindromes in the range from 1 to `n` (inclusive) using a `for` loop. It iterates through each number and checks if it's a palindrome by comparing the string representation of the number with its reverse using the slice notation `str(i) == str(i)[::-1]`. If it's a palindrome, it checks if the number is even or odd to update the respective count.

The script should work seamlessly for the specified problem and fulfill the given conditions.