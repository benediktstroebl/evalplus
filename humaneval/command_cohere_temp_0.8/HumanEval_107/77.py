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

The `even_odd_palindrome` function takes in a positive integer `n` and aims to determine the count of even and odd integer palindromes in the range from 1 to `n`. It initializes two counters, `even` and `odd`, to zero to keep track of the number of even and odd palindromes, respectively. It then iterates through the range from 1 to `n` (inclusive) and examines each integer `i`. If `i` is a palindrome (i.e., reads the same backward and forward), it increments the appropriate counter based on whether `i` is even or odd. Finally, the function returns a tuple containing the counts of even and odd palindromes.