Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_odd = 0
    count_even = 0
    temp_num = str(num)
    for i in temp_num:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

To ensure that the function works smoothly, it checks for edge cases like num == 0 and returns (0, 0) if the input is 0. Also, temp_num is used to convert the input num into a string, so that the funciton can easily iterate over its digits. The iteration uses a for loop to determine if each digit is even or odd and accordingly increments count_even or count_odd.

This function can be tested quite easily. Here is a test suite that can be used:
```python
# Testing the even_odd_count function
def test_even_odd_count():
    # Test case 1: Should return (1, 1)
    assert even_odd_count(-12) == (1, 1)

    # Test case 2: Should return (1, 2)
    assert even_odd_count(123) == (1, 2)

    # Test case 3: Should return (0, 0)
    assert even_odd_count(0) == (0, 0)

    # Test case 4: Should return (3, 2)
    assert even_odd_count(672) == (3, 2)

test_even_odd_count()
```

This test suite contains 4 test functions to check 4 different scenarios. The assert statements will ensure that the test_even_odd_count function returns the expected outputs.

The complete code will look like:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_odd = 0
    count_even = 0
    temp_num = str(num)
    for i in temp_num:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)

# Testing the even_odd_count function
def test_even_odd_count():
    # Test case 1: Should return (1, 1)
    assert even_odd_count(-12) == (1, 1)

    # Test case 2: Should return (1, 2)
    assert even_odd_count(123) == (1, 2)

    # Test case 3: Should return (0, 0)
    assert even_odd_count(0) == (0, 0)

    # Test case 4: Should return (3, 2)
    assert even_odd_count(672) == (3, 2)

test_even_odd_count()
``` 

This code can be copied and pasted into a Python environment or script to test and use the even_odd_count function as required.