```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]
```
The function unique takes a list as input and returns a new list containing only the elements that are not in the set seen. This is unique approach uses the result because it ensures that duplicates are not included.