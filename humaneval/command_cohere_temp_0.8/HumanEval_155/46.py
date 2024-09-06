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
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function uses a string representation of the input number to iterate through each digit and determines whether it is even or odd, incrementing the respective count variable. The function handles cases like '-' or ' ' as seen in the examples and returns a tuple with the counts.

Here is a test suite to ensure that the function behaves as expected:
```python
# Testing the even_odd_count function
def test_even_odd_count():
    # Test case 1: Should return (1, 1)
    assert even_odd_count(-12) == (1, 1)

    # Test case 2: Should return (1, 2)
    assert even_odd_count(123) == (1, 2)

    # Test case 3: Should return (2, 1)
    assert even_odd_count(488) == (2, 1)

    # Test case 4: Should return (0, 2)
    assert even_odd_count(0) == (0, 2)

    # Test case 5: Should return (2, 0)
    assert even_odd_count(198) == (2, 0)

    # Test case 6: Should return (0, 1)
    assert even_odd_count(101) == (0, 1)

test_even_odd_count()
```

Running the test suite will ensure that the function behaves as expected, giving a clear indication of whether or not the code is correct.  If the tests pass, you can be confident that the function is working correctly. Feel free to ask any more questions or request further assistance!