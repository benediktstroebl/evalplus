Here's a Python script that contains a function named `even_odd_palindrome` which addresses the problem you've outlined
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

The function employs a simple loop to traverse through all numbers between 1 and `n` (`inclusive`). When it encounters a palindrome, it checks whether it's even or odd and increments the respective counter. The final count is then returned as a tuple. 

This code should work seamlessly for the given input range and provide the correct count of even and odd palindromes. Feel free to test it against the provided examples or other cases you might imagine.  If you'd like to test this function's correctness, you can use the following example test cases

```python
# Test Case 1
print(even_odd_palindrome(3))  # Output: (1, 2)

# Test Case 2
print(even_odd_palindrome(12))  # Output: (4, 6)
```