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
        raise TypeError("Input must be an integer")
```

And here is a test suite that can be used to validate the function above:
```python
import unittest

def test_even_odd_count():
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(14) == (0, 1)
    assert even_odd_count(1234) == (2, 2)
    assert even_odd_count(43) == (0, 1)
    assert even_odd_count(11) == (1, 0)
    assert even_odd_count(10) == (1, 0)
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-14) == (0, 1)
    assert even_odd_count(-1234) == (2, 2)
    assert even_odd_count(-43) == (0, 1)
    assert even_odd_count(-11) == (1, 0)
    assert even_odd_count(-10) == (1, 0)
    assert even_odd_count(-1) == (0, 1)
    assert even_odd_count(-0) == (0, 0)

if __name__ == '__main__':
    unittest.main()
```

The test suite contains a test function that tests the even_odd_count function with a variety of input integers and the expected counts of even and odd digits. When the code is run, the tests are automated with the unittest framework. If the tests pass, this will output, "test_even_odd_count.py ......OK", indicating that all tests have passed and the function works as intended.  Any other output would mean at least one test has failed and the function is not working correctly. 

To run the test suite, you can copy and paste the test code into a Python file (e.g. test_even_odd_count.py) and run the file. You can do this by using the following command:
```bash
python test_even_odd_count.py
```

Alternatively, you can also navigate to the directory containing the .py file and use the following command:
```python
python test_even_odd_count.py
```

This will run the test file and report the results, indicating the tests that passed or failed.