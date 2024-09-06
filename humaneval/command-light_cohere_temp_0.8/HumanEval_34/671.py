```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [''] and x]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert unique(test_list) == [0, 2, 3, 5, 9, 123]
 ```
This script defines a function called unique that takes a list as an argument and returns a new list containing only the unique elements from the original list. The seen set is used to keep track of elements that have already been seen, and the condition that an element must satisfy to be considered unique is that it is not in the seen set, not in the string, and not an empty string.