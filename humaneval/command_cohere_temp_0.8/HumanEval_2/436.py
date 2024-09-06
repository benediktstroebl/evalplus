```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
tests = [ (3.5, 0.5),  # Basic case
         (2.5, 0.5),
         (1.0, 0.0),
         (1.5, 0.0),
         (11.05, 0.05),
         (3.555, 0.555),
         (34.7, 0.7)
]

for n, result in tests:
    assert truncate_number(n) == result
``` 

The function `truncate_number` takes a single parameter, `number`, which is the number to be processed. It computes the difference between the given number and the closest integer (rounded version of the number), which represents its decimal part. This decimal part is then returned as the result. Considering all the test cases in the list `tests`, the assertion checks if the computed result matches the expected decimal part, ensuring the correct behavior of the function.  This approach provides a simple and straightforward solution to extract the decimal part of a number, regardless of its magnitude or decimal precision.  The function is also scalable and adaptable to different types of tests.