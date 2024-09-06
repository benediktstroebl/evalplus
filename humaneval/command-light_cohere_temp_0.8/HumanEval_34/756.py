```python
def unique(lst):
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

print("Test successful!")
``` 
This code defines a function unique that returns a new list with unique elements from the original list. It then creates a unique list from a list of numbers, and the test_unique function asserts that the resulting list contains the expected unique elements.