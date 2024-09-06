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
         (41.5, 0.5),
         (51.67, 0.67),
         (101.05, 0.05),
         (301.03, 0.03)
       ]

for n, expected in tests:
    assert truncate_number(n) == expected
```

The function `truncate_number` takes a single parameter, `number`, which is the number to be processed. It computes the difference between the given number and the closest integer (rounded version of the number), which represents the decimal part of the decomposition. This decimal part is then returned as the result. 

The test suite aims to validate the function's behavior across different scenarios. A variety of numbers are input, ranging from integers to floats with varying degrees of accuracy. For each input, the expected decimal portion is computed independently and compared against the function's output through the `assert` statement, ensuring the intended behavior is maintained. 

The script can be executed independently, and the tests can be run collectively to validate the functionality.  The resulting output, preceded by a `PASS' message for each successful test and failure messages in case of failures, would provide confidence in the function's correct operation. 
```python
for test in tests:
    n, expected = test
    output = truncate_number(n)
    print(f'Test {n}, expected {expected}, output {output}, equal?: {expected == output}')
    assert expected == output
```