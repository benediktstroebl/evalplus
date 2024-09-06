Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

This function takes a positive integer `n` as input and aims to calculate the number of even and odd integer palindromes within the range from 1 to `n`. The function uses a loop to iterate through numbers from 1 to `n` and checks if each number is a palindrome by converting it to a string and comparing it with its reverse. If the number is a palindrome and its parity is even, the `even` count is incremented; otherwise, the `odd` count is incremented. The function finally returns a tuple containing the counts of even and odd palindromes.

The unit test section contains tests to verify the correct behavior of the function:
```python
# Unit tests:
def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(100) == (49, 51)

test_even_odd_palindrome()
```

You can incorporate these tests into your script to ensure the function behaves as expected. I hope this solution helps solve your problem effectively! Let me know if you have any further questions.