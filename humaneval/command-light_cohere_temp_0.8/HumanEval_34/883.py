```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]

if __name__ == "__main__":
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(lst))  # Output: [0, 2, 3, 5, 9, 123]
``` 
The function unique takes a list lst as input and returns a new list containing only the elements that are not in the set seen. It uses the unique elements by utilizing the set() data structure to keep track of elements that have already been seen. This ensures that duplicate elements are automatically skipped.