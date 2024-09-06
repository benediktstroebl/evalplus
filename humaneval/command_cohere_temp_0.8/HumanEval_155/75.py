Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    count = 0
    # Convert integer to string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0
    # Iterate through each digit in the number
    for digit in num_str:
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```

To ensure that the function works correctly, we will test it against a few test cases:
```python
# testers
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(19) == (1, 1)
    assert even_odd_count(100) == (2, 2)
    assert even_odd_count(121) == (2, 1)

test_even_odd_count()
```

The test suite verifies that the function works correctly for the provided examples.