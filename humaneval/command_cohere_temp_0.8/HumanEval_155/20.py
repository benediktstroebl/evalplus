Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    return (count_even, count_odd)
```

This function converts the input num to a string and iterates through each digit. It counts the number of even and odd digits, and returns a tuple containing both counts. The code includes a base case where if the input num is 0, it returns 0 for both counts. 

Here is a simple test case to verify the functionality of the function:
```python
def test_even_odd_count():
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(78) == (2, 1)
    assert even_odd_count(err123) == (1, 1)
    assert even_odd_count(0) == (0, 0)

test_even_odd_count()
```

Ensure you have the desired version of Python installed to execute the code and pass the test. Let me know if you have any questions or if you'd like to proceed to additional problems or clarifications!