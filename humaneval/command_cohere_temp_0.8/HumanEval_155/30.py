Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
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
    else:
        raise ValueError("Input must be an integer")
``` 

And here is a test suite that can be used to validate the functionality:
```python
def test_even_odd_count():
    assert even_odd_count.even_odd_count(-12) == (1, 1)
    assert even_odd_count.even_odd_count(123) == (1, 2)
    assert even_odd_count.even_odd_count(15) == (2, 1)
    assert even_odd_count.even_odd_count(800) == (5, 3)
    assert even_odd_count.even_odd_count(21874878383) == (6, 5)
    assert even_odd_count.even_odd_count(9876543210) == (3, 5)

test_even_odd_count()
```

The test suite contains a single test function that calls the even_odd_count() function with different input values and verifies that the returned values are correct.

Note, this code assumes that the input is a valid integer and will raise a ValueError if the input is not an integer. Adjustments can be made to handle other edge cases if needed.