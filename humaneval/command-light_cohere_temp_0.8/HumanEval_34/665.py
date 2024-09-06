```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -elf, -ilIST]]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([12]) == []
assert unique([12, 12]) == [12]

```
This Python code defines a function unique that takes a list as input and returns a new list containing unique elements from the original list. The function uses a set seen to keep track of elements that have been encountered, and it iterates through the input list, using the condition (not in seen) and the set membership test to filter out duplicates. The test cases demonstrate the