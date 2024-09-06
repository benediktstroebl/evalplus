Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you have described:
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
This function counts the number of even and odd integer palindromes within the range(1, n), and returns a tuple containing these two counts. The function uses a loop to iterate through numbers from 1 to n, converts each number to a string and checks if it is a palindrome. If it is a palindrome, the function checks if the string length is even to determine if it is an even palindrome or odd palindrome. The function then returns a tuple with the counts of even and odd palindromes, respectively.