Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = str(abs(num))
    for i in temp_num:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

This script defines a function named `even_odd_count` which takes a single argument, num, representing an integer. The function converts the input to an absolute value and converts it to a string. Then, it iterates through the string representation of the number, counting the number of even and odd digits encountered. Finally, it returns a tuple (count_even, count_odd) representing the counts of even and odd digits, respectively.

Here is a simple test suite to verify the functionality of the above function:
```python
def test_even_odd_count():
    # Test case insensitivity
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)

    # Test with a single digit
    assert even_odd_count(5) == (0, 1)

    # Test with a number with multiple digits
    assert even_odd_count(125) == (1, 2)

    # Test with a large number
    assert even_odd_count(12345678) == (3, 5)

test_even_odd_count()
```

The test suite contains several tests to validate the behavior of the `even_odd_count` function for different input scenarios.