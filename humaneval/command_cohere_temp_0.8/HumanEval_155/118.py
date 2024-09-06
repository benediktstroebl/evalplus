Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp = str(num)
    if temp[0] == '-':
        temp = temp[1:]
    for char in temp:
        if char >= '0' and char <= '9':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function uses a string representation of the input number to iterate through each digit and determine if it is odd or even. It then returns a tuple containing two elements – the number of even digits and the number of odd digits respectively.

Here is a simple test suite to ensure the functionality:
```python
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (2, 1)
    assert even_odd_count(19) == (1, 2)
    assert even_odd_count(0) == (1, 0)

test_even_odd_count()
```

The test suite contains a few test cases that cover different scenarios.