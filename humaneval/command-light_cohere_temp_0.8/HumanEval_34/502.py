Here is a Python script that includes the unique function:

```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

#Test case 1
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
def test_unique_empty():
    assert unique([]) == []

# Test case 3
def test_unique_duplicates():
    assert unique([3, 3]) == [3]

if __name__ == "__main__":
    test_unique()
    test_unique_empty()
    test_unique_duplicates()
```

Please, feel free to use this script and let me know if you have any further questions or require additional assistance.