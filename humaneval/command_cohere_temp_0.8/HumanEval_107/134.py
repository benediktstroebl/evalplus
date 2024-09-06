Here's a Python script that includes a function to solve the given problem:
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
This script defines the `even_odd_palindrome` function, which takes in a positive integer `n` as input and returns a tuple containing the counts of even and odd integer palindromes within the range of 1 to `n` inclusive.

The script achieves this by:
- Initializing two variables, `even` and `odd`, to 0 for tallying the counts of even and odd palindromes, respectively.
- Iterating through numbers from 1 to `n` using a `for` loop.
- Converting each number `i` to a string `s` and checking if it's a palindrome by comparing it to its reverse (`s[::-1]`).
- Checking if the converted string back to an integer retains the original value.
- If the checks pass, the script increments the appropriate counter based on whether the palindrome's length is even or odd.

The script then returns a tuple (`even`, `odd`) containing the counted even and odd palindromes, respectively. Overall, this code efficiently solves the problem and provides the required counts of even and odd palindromes within the specified range.