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

def test_single_item():
    assert unique( [5]) == [5]

if __name__ == "__main__":
    test_unique()
    test_empty()
    test_single_item()
```
This script defines a function `unique` which takes a list as an argument and returns a new list with unique elements from the original list, the function also contains several tests to validate the functionality of the `unique` function. 
The tests use the specific inputs and assert the output matches the expected result.