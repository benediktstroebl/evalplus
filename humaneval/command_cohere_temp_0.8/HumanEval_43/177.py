```python
def pairs_sum_to_zero(l):
    # Count the number of pairs
    count = len(l) - l.count(0) // 2
    # Return true if there are exactly two pairs that sum to zero
    return count == 2
```

This function uses the fact that a list of integers contains pairs that sum to zero when there are an even number of elements and exactly two distinct elements sum to zero. For example, the list `[1, -1, 2, -2]` has four elements, so there must be two pairs that sum to zero, which are `1 + (-1) = 0` and `2 + (-2) = 0`. 

The function first calculates the number of pairs of elements in the list using `len(l) - l.count(0) // 2`. Then it returns `True` if this count is exactly 2, and `False` otherwise.

Here is a Markdown code block containing a simple test suite with example inputs and expected outputs that can be used to verify the function:
```yaml
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```

To run the test suite, you can use a testing framework like `pytest`. If you have `pytest` installed, you can run the test suite by saving the code blocks above in a file called `test_pairs_sum_to_zero.py` and then running the following command in your terminal:
```bash
pytest test_pairs_sum_to_zero.py
```

This will run the test suite and print out a summary of the results. 

Here's what the test suite looks like when formatted as YAML:
```yaml
--- 
  - 
    - Expected: False 
     Content: pairs_sum_to_zero([1, 3, 5, 0]) 
  - 
    - Expected: False 
     Content: pairs_sum_to_zero([1, 3, -2, 1]) 
  - 
    - Expected: False 
     Content: pairs_sum_to_zero([1, 2, 3, 7]) 
  - 
    - Expected: True 
     Content: pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) 
  - 
    - Expected: False 
     Content: pairs_sum_to_zero([1])
```
```