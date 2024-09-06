```python
def unique(lst):
    return list(set(lst))

def test_unique(*args):
    assert len(unique(args)) == len(args), "Length of returned list does not match input list length"
    assert all(type(item) == int for item in unique(args)), "Returned list contains non-integers"
    return unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

if __name__ == "__main__":
    test_unique(5, 3, 5)
    test_unique(2, 3, [2, 3, 0, 3])
    test_unique(123, [0, 2, 3, 5, 9])
```
This code defines a function unique that returns a new list with unique elements from the input list. The test_unique function contains various tests to ensure the correctness of the unique function. The main function is invoked to run these tests.