```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the nearest integer, which represents the residual decimal part of the original number. 

To test this script, you can create a test case like this:
```python
>> import unittest
>> test = unittest.TestCase()
>> test.assertEqual(truncate_number(3.5), 0.5)
>> test.assertEqual(truncate_number(2.8), 0.2)
>> test.assertEqual(truncate_number(5.0), 0)
>> test.assertEqual(truncate_number(0.1), 0.1)
>> test.assertEqual(truncate_number(10.5), 0.5)
>> unittest.main()
``` 
Make sure to have the `unittest` module imported in order to run the tests and verify the correct behavior of the `truncate_number` function.  This way, you can validate that the script produces the expected output for different inputs.  By running `unittest.main()` at the end, the script executes the test suite and displays the test results.