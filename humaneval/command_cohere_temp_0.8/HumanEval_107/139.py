Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range of 1 to `n` inclusive, in a markdown code block:
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

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to determine the count of even and odd integer palindromes within the range of 1 to `n`. It initializes two counters, `even` and `odd`, to zero to keep track of the number of even and odd palindromes, respectively. Then, it iterates through the range of 1 to `n` (inclusive), checking if each integer `i` is a palindrome by comparing its string representation with its reverse (`str(i) == str(i)[::-1]`). If it is a palindrome, it checks if `i` is even or odd to update the respective counter accordingly. Finally, the function returns a tuple containing the counts of even and odd palindromes.