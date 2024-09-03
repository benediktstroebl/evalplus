```python
def sum_to_n(n: int):
    """
    Sums numbers from 1 up to n.
    :param 
    n: int (number up to which we want to sum)
    :return: int (total sum of the numbers from 1 to n)
    """
    return sum(range(1, n+1))

# Test function for sum_to_n
def test_sum_to_n():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1

# Run the test function to verify the implementation
test_sum_to_n()
```
This code defines a function `sum_to_n` that calculates the sum of numbers from 1 up to a given integer `n`. The function uses the sum function along with the range function to achieve the result. 

The code also includes a test function `test_sum_to_n` that checks the correctness of the `sum_to_n` function by passing various input values and asserting the results against the expected values. 

Finally, the `test_sum_to_n` function is called to run the tests.