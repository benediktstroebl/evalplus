```python
def count_palindromes(n):
    # create two counters to count even and odd length palindromes
    even, odd = 0, 0

    # iterate through possible palindromes from 1 to n
    for l in range(1, n + 1):
        # check if the current number is a palindrome
        if l == int(str(l)[::-1]):
            # if it is, increment the counter for its parity
            if l % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

# Driver code
n = int(input())
even, odd = count_palindromes(n)
print(f'({even}, {odd})')
```

This script includes a function `count_palindromes(n)` that takes in a positive integer `n` as input and returns a tuple containing the number of even and odd-length palindromes within the range of 1 to `n` inclusive. The driver code reads in the value of `n` from the input, calls the function, and prints the result.