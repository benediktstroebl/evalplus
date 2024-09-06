Here is a self-contained Python script that solves the problem of returning unique elements in a list:
```python
def unique(lst):
    return list(set(lst))

# Test cases
 tests = [
    [list(map(int, "abc"))],
  [],
  [5, 3, 5, 2, 3, 3, 3, 9, 0, 123],
  [(), True],
  [1, 2, 3],
]

# Function call
for test in tests:
    assert unique(test) == test[1]
``` 
This script defines a function unique that takes a list as input and returns a new list containing only the unique elements from the input list. The function achieves this this by converting the list to a set and then back to a list. This ensures that no duplicate elements are present in the returned list. 

The script also provides a set of test cases to verify the correctness of the `unique` function.