Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes in the range of 1 to `n` inclusive. The code tests run successfully:
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

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to calculate the count of even and odd integer palindromes in the range from 1 to `n` inclusive. It initializes two counters, `even` and `odd`, to 0 to keep track of the number of even and odd palindromes, respectively. Then, it loops through the numbers from 1 to `n` using the `for` loop with the `range()` function. For each number `i`, it checks if the string representation of `i` is the same when reversed (`str(i) == str(i)[::-1]`), which indicates that `i` is a palindrome. If the number is even, both the odd and even counters increase, and if the number is odd, only the `odd` counter increases. Finally, the function returns a tuple containing the calculated counts of even and odd palindromes.