Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
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

And here is a test suite to ensure that the function correctly solves the problem:
```python
# Tests
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(10) == (2, 0)
    assert even_odd_count(100) == (2, 2)
    assert even_odd_count(999) == (3, 3)
    assert even_odd_count(10000) == (4, 2)
    assert even_odd_count(987654321) == (6, 5)

test_even_odd_count()
```

Leave a line empty or provide any additional comments or requests you may have!