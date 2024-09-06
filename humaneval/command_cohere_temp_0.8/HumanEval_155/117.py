Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_ev = 0
        count_od = 0
        str_num = str(num)
        for char in str_num: 
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_ev += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_od += 1
        return (count_ev, count_od)
    else:
        return "Error: Please enter an integer!"
```

And here is a test suite that checks if the function behaves as expected with an example prompt and corresponding test case:
```python
# Test suite
def test_even_odd_count():
    # Example test case
    num = -12
    expected_result = (1, 1)
    result = even_odd_count(num)
    assert result == expected_result  # Assertion passes, test case is successful
    
test_even_odd_count()  # Call the test function to execute the test case
```

When you run this test suite with an IDE or testing framework, it will execute the test case and verify that the assertion passes, indicating that the even_odd_count function behaves as expected.  This will ensure that the function's behavior matches the specified problem statement.  If the test fails, it will provide you with insight into what aspect of the function's behavior is incorrect.  This helps to ensure that the script behaves as expected, providing the right count of even and odd digits.