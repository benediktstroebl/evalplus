Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8' or char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

And here is a test suite to make sure the function behaves as expected:
```python
def test_even_odd_count():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(1000) == (3, 7)
    assert even_odd_count(657) == (3, 4)
    assert even_odd_count(0) == (0, 0)

test_even_odd_count()
```

The test suite provides a few test cases to cover different scenarios and ensure the function behaves as expected. You can add more test cases as needed to cover other edge cases and further verify the function's correctness.