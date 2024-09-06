```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]
 
if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Result:", unique(test_list))
```
This code defines a function called unique that takes a list lst as input and returns a new list containing only the unique elements from the original list. It uses a unique elements in a list to store unique elements and the set to check if an element is already in the unique set. The function iterates over the unique elements in the list, and adds them to the unique elements set if they are not already present. The function then returns a list containing only the unique elements. The code then executes this test list, and the result is printed.