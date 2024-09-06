```python
def unique(lst):
    return list(set(lst))

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Driver code
if __name__ == "__main__":
    test_unique()
```
The function `unique` returns a new list containing only the unique elements of the original input list. The test case ensures that the function behaves as expected and produces the correct output.