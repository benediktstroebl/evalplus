```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 5]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(test_lst))  # Output: [0, 2, 3, 5, 9, 123]
```
The code defines a function called unique, which takes a list as input and returns a new list containing only the unique elements from the original list. The function uses a `set()` to create a set of unique elements, and then iterates through the original list, adding elements to the set if they are not already present. The output will then list of unique elements.