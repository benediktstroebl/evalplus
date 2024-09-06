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

This function takes a positive integer `n` as input and returns a tuple containing two counts: the number of even and odd integer palindromes, respectively, that fall within the range of 1 to `n` (inclusive). The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it to its reverse. If the number is a palindrome and its parity (whether it is even or odd) matches the provided parity, the respective count is incremented.

The provided tests in the markdown code block can be automated using a unit testing framework like `pytest`. Here's an example of how you can use `pytest` to automate and execute those tests:
```python
def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (49, 51)
```

This will automatically run the tests and verify that the function's behavior aligns with the expected output for the provided inputs.