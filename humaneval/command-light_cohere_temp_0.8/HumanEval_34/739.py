```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_empty():
    assert unique([]) == []

def test_single():
    assert unique( [123]) == [123]

if __name__ == "__main__":
    test_unique()
    test_empty()
    test_single()
```

This Python script defines a function `unique` that returns a list with unique elements from the input list. It also includes four test functions to check the functionality of the `unique` function with various inputs.