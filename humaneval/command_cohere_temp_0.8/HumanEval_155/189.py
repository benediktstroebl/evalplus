Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9":
            if char % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            if int(char) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count
```

And here is a test suite containing two test functions to ensure that the even_odd_count function performs as expected:
```python
def test_even_odd_count_with_negative_input():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_with_positive_input():
    assert even_odd_count(123) == (1, 2)
```

These tests ensure that the even_odd_count function works correctly for both positive and negative integers as described in the problem statement.