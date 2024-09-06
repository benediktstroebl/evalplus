Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9" or char < "0":
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

And here is a test suite to make sure the function behaves correctly:
```python
def test_even_odd_count():
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(15) == (0, 3)
    assert even_odd_count(108) == (3, 3)
    assert even_odd_count(8000) == (6, 4)
    assert even_odd_count(-20) == (1, 2)
    assert even_odd_count(0) == (1, 0)

test_even_odd_count()
```

The test suite contains one function with multiple assertions that test the even_odd_count function with different input values.