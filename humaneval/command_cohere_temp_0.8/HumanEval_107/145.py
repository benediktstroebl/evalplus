```python
def count_palindromes(n):
    # dictionary to count the number of palindromes
    # with odd numbers at the beginning and end
    odd = 0
    # with even numbers at the beginning and end
    even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i%2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd
```
The `count_palindromes` function uses two nested loops to iterate through all numbers between `1` and `n`. It checks if each number is a palindrome by comparing the string representation of the number with its reversed version. 

If the number is a palindrome and its parity is even, the `even` variable is incremented; if the number is a palindrome and its parity is odd, the `odd` variable is incremented. Finally, the function returns a tuple containing the counts stored in the `even` and `odd` variables. 

This solution has a time complexity of `O(n^2)`, where `n` is the given number since it iterates through all numbers between `1` and `n` and performs a constant-time operation for each number.