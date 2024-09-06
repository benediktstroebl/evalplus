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
This Python script defines a function even_odd_palindrome that takes in a positive integer n as input and returns a tuple containing the counts of even and odd integer palindromes within the range(1, n+1) inclusive. It achieves this by iterating through all numbers from 1 to n, checking if each number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome and an even number, it adds 1 to the even count; if it is a palindrome and an odd number, it adds 1 to the odd count. The script ensures that the counts are correctly calculated and returned as a tuple, as specified in the given problem.