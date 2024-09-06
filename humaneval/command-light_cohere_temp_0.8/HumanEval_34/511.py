```python
def unique(l: list):
    seen = set()
    return [x for x in l if not in seen and x not in [-None, float('inf')] and not in [-0, float('inf')] and x not = None]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(test_list) == [0, 2, 3, 5, 9, 123]
    test_list = [5, 3, 'a', 5, 3, 'b']
    assert unique(test_list) == ['a', 'b']
    test_list = [5, 3, -1, -2, float('inf')]
    assert unique(test_list) == [-1, -2]
```
This Python script defines a function named unique that takes a list l as input and aims to return a list of unique elements from l, excluding None, float('inf'), and negative numbers. The function utilizes a basic set theory to track seen elements and iterates through the input list, adding elements to the set if they are unique and not previously seen. The function then returns a set of unique elements from the input list.