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
This Python script defines a function even_odd_palindrome that takes a positive integer n as input and returns a tuple containing the counts of even and odd integer palindromes in the range [1, n]. It uses a loop to iterate through all numbers from 1 to n, checks if each number is a palindrome by comparing its string representation with its reverse, and then increments the appropriate count based on whether the number is even or odd. The function returns a tuple (even, odd) containing the counts of even and odd palindromes, respectively.