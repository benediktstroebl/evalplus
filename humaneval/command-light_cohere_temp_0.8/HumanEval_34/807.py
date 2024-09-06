```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_single_item():
    assert unique([5]) == [5]

def test_empty_list():
    assert unique([]) == []

def test_many_items():
    assert unique([3, 3, 4, 9, 9, 2, 6, 6]) == [3, 4, 9, 2]

if __name__ == "__main__":
    test_unique()
    test_single_item()
    test_empty_list()
    test_many_items()
```
This code includes a function unique that takes a list as input and returns a new list with unique elements from the original. It uses a generate a set to keep track of elements seen so far and then use a for loop to go through the list and append elements to the result list if they are not in the set. This ensures that all elements are unique and don't duplicate. 

The test functions are used to verify the correctness of the unique function.