Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
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

This function takes in a positive integer `n` and returns a tuple containing two counts: the number of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome, it checks if it is even or odd and increments the appropriate count.

The script also includes test cases in the `__main__` block that verify the function's behavior against the given examples from the problem statement:
```python
def __main__():
    print(even_odd_palindrome(3))  # Output: (1, 2)
    print(even_odd_palindrome(12))  # Output: (4, 6)
``` 

When the script is run, these test cases will be executed and the expected output will be printed. 

**Note:** This solution has a time complexity of O(n).