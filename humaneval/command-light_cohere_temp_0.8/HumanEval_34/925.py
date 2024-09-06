Here is a Python script that includes the unique function along with its corresponding tests:
```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

def test_unique():
    """Functional test for unique function"""
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Run the tests when the script is executed
test_unique()

```
The script defines a function called unique, which takes a list as an argument and returns a new list containing the unique elements from the original list. It also includes a test_unique function that creates a test case for the unique function and asserts the result of calling unique on a list of known values.