Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

The function takes a positive integer `n` as input and calculates the number of even and odd integer palindromes in the range `[1, n]` using a loop. It then returns a tuple containing these two counts. The test cases provided in the Markdown code block can be used for verification.  This code should be contained within a code block with markdown syntax:
```python
```
This code will provide the counts of even and odd-integer palindromes for the specified range.  You can customize the code to suit your needs or modify it to handle larger test cases if necessary. Let me know if you would like me to make any additional comments on the code or explain any part in more detail!