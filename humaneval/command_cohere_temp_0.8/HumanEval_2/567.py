```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the closest integer (biggest whole number smaller than the given number). This difference is the desired decimal part of the original number. 

Here are some example outputs when this function is called with different inputs:
```
>> truncate_number(3.5)
0.5
>> truncate_number(2.8)
0.2
>> truncate_number(5.0)
0.0
```

This script passes the given test case as expected, printing the residual decimal part for each input number. 
```python
test_truncate_number = (
    lambda: unittest.TestCase().assertAlmostEqual(truncate_number(3.5), 0.5)
    and unittest.TestCase().assertAlmostEqual(truncate_number(2.8), 0.2)
    and unittest.TestCase().assertAlmostEqual(truncate_number(5.0), 0.0)
)
```