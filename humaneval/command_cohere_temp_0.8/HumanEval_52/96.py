```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x` and compare it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, meaning that all numbers in the list are below the threshold, and `below_threshold()` returns `True`. If not, it returns `False`. 
The expected behavior for the given test cases is:
- `below_threshold([1, 2, 4, 10], 100) -> True`
- `below_threshold([1, 20, 4, 10], 5) -> False` 

Here is a Markdown code block with corresponding test cases to verify the correct functionality of the function:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100), "All numbers below threshold"
    assert not below_threshold([1, 20, 4, 10], 5), "All numbers below threshold"
    assert below_threshold([0, 0, 0], 1), "All numbers below threshold"
    assert not below_threshold([1, 1, 1], 1), "All numbers below threshold"
    assert below_threshold([2**63-1, -2**63, 0], 2**63-1), "All numbers below threshold"
```

You can then check the functionality of the function by running the test cases using the appropriate testing framework, like `pytest`:
```bash
pytest -vv test_below_threshold.py
```
This will verify that the function behaves as expected and correctly determines whether all numbers in the list are below the threshold.