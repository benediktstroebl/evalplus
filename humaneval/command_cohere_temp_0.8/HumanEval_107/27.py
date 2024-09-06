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

This function relies on a loop to iterate through all numbers from 1 to `n` (inclusive) and assesses whether each number is a palindrome by comparing its string representation with its reverse. When a palindrome is encountered, it is labeled as either even or odd depending on its parity, and the appropriate count is increased by one. Ultimately, the function returns a tuple containing the counts of even and odd palindromes. 

The unit tests for this function can be crafted to validate its behavior across a range of scenarios. For instance, you might simulate various input values and compare the returned tuples with the expected counts of even and odd palindromes. Here's an illustration:
```python
# Test Case 1
n = 3
expected_output = (1, 2)
result = even_odd_palindrome(n)
assert result == expected_output

# Test Case 2
n = 12
expected_output = (4, 6)
result = even_odd_palindrome(n)
assert result == expected_output
```

You can generate additional test cases to cover a spectrum of inputs and confirm the accuracy of the `even_odd_palindrome` function.