Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range from 1 to `n`:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function takes in a positive integer `n` and aims to determine the count of even and odd integer palindromes in the range from 1 to `n`. To do so, it initializes two counters, `even` and `odd` to 0, and then iterates through the numbers from 1 to `n` using the `range` function. For each number `i`, it checks if the string representation of `i` is the same when reversed (`str(i) == str(i)[::-1]`), which indicates that `i` is a palindrome. If the palindrome is divisible by 2, it increments the `even` counter; otherwise, it increments the `odd` counter. Finally, the function returns a tuple containing the calculated counts of even and odd palindromes.