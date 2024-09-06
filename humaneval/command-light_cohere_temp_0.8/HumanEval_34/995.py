```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-]+]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Result:", unique(test_list))

    test_seen = set()
    print("Test seen:", test_seen)

    expected = [0, 2, 3, 5, 9, 123]
    print("Expected:", expected)

    assert unique(test_list) == expected
    assert test_seen == set(expected)
```
The function `unique` accepts a list as an argument and returns a new list containing the list's unique elements. The function utilizes a unique property of the set data type, which stores unique elements only, to efficiently filter out duplicate elements from the input list.