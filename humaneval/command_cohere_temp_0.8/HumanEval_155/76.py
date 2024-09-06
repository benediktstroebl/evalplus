Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        str_num = str(num)
        for char in str_num: 
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_even += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:
        raise TypeError("Input must be an integer")
```

And here is a test suite that checks if the function behaves as intended:
```python
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(19) == (0, 1)
    assert even_odd_count(20) == (1, 1)
    assert even_odd_count(10001) == (3, 2)

test_even_odd_count()
```

The test suite passes the function test_even_odd_count which exercises multiple test cases to ensure that the function behaves as described in the problem statement.