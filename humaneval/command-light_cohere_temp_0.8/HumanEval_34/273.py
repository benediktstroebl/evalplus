```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 4]

#Test case 1: Unique elements in a list
assert(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])

#Test case 2: Recursively dealing with lists
assert(unique([[1, 2, 3], [4, 5], [6, 7], [8, 9]]) == [[1, 2, 3, 4, 6, 7, 8, 9]])

#Test case 3: Removing duplicates and empty elements
assert(unique([3, 5, 2, 1, 2, 4, 6, 7]) == [2, 3, 4, 5, 6, 7])
```
The code defines a function called unique which takes a list as input and returns a new list containing unique elements from the original list, while ignoring duplicates and empty elements. It utilizes a unique and set-based method to keep track of unique elements. The test cases aim to validate the correctness of the function by checking if it returns the correct set of unique elements in the corresponding input lists.