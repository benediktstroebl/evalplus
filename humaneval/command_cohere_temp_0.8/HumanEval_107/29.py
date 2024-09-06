Here's a Python script that contains a function named `even_odd_palindrome` designed to address the given problem:
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

The function `even_odd_palindrome(n)` employs a loop to traverse numbers from 1 to `n` and checks if each number is a palindrome. When a palindrome is encountered, the function examines whether it's even or odd, updating the respective count accordingly. The function ultimately returns a tuple containing the counts for even and odd palindromes.

This script adheres to the problem's specifications, and the provided function should effectively tackle the posed problem while passing any inherent tests. Feel free to incorporate this function into your solution, and let me know if you require further customization or additional assistance!