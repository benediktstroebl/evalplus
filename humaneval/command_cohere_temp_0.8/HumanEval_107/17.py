Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range(1, n+1), the function is further explained below:
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
The function initiates two counters, `even` and `odd`, to zero at the start of the function. It then iterates through numbers from 1 to `n` and checks if each number is a palindrome. If the number is a palindrome and its parity (whether it is even or odd) matches the requirement, the respective counter is incremented. 

Finally, the function returns a tuple containing the two counters. This approach ensures that the function is self-contained and does not rely on any global variables or external assumptions. 

The `even_odd_palindrome` function should work correctly for positive integers `n` within the specified range (1, 10^3).