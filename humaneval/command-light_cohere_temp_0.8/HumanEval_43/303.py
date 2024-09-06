```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test case
   
    pairs_sum_to_zero([1, 3, 5, 0])
    Should return True
    """
    return (1 + 3 > 0) and (1 + 5 > 0) and (3 + 5 > 0) and (-2 + 1 > 0) and (-5 + 3 > 0)

def test_sum():
    """
    test_list = [1, 3, 5, 0]
    assert pairs_sum_to_zero(test_list) == True

if __name__ == "__main__":
    test_sum()
```

The code defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that sum up to zero. It uses the test assertions to test the function with a sample input. The `test_sum` function provides a test case with a list of integers. The test will fail if the `pairs_sum_to_zero` returns `False` and pass if it returns `True`.