```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == 0]

# Test case 1: Ensure it works with non-list types and 0
def test1():
  result = unique([5, 3, 5, 2, 3, 3, 9, 0])
  assert result == [0, 2, 3, 5, 9, 123]

# Test case 2: Ensure it works with lists of various lengths
def test2():
  shorter = [5, 3, 9]
  longer = [123, 2, 3, 5, 6]
  result = unique(shorter + longer)
  assert result == [0, 2, 3, 5, 6] + [9]

# Test case 3: Ensure duplicates are handled correctly
def test3():
  result = unique([5, 3, 5, 3])
  assert result == [0, 2, 3, 5, 123]
```
This Python code defines a function called unique that takes a list as input and returns a new list containing unique elements from the original list. The function uses a approach of creating a set to keep track of elements seen so far and then iterates through the original list, adding elements that are not in the set and are not equal to zero. The code also provides three test cases to verify the correctness of the unique function.