```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not(set() == seen)]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    unique_test = unique(test_list)
    print("Test list:", test_list)
    print("Unique elements:", unique_test)
    print()

    assert set(unique_test) == set([0, 2, 3, 5, 9, 123])
``` 
Do you require any other assistance with implementing your code or would you like to explore other topics in Python?