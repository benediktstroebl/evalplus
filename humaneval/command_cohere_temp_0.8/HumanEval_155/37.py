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
            even_count += 1
    return (even_count, odd_count)
```

The function uses a simple algorithm that takes an integer and converts it to a string. Then, it counts the number of even and odd digits in the string, adding the count to the respective variables. The function returns a tuple with the even and odd counts.

Here is a test suite to ensure that the function behaves as expected:
```python
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (2, 1)
    assert even_odd_count(19) == (1, 1)
    assert even_odd_count(100) == (2, 2)
    assert even_odd_count(121) == (2, 1)
```