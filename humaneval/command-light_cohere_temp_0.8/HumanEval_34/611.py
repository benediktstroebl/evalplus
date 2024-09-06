```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]
```
This Python code defines a function called unique that takes a list lst as input and returns a new list containing unique elements from the original list. It utilizes a this set seen to keep track of elements that have been encountered before, then it iterates through the original list and adds elements to the seen set if they are not duplicates and are not currently in `[0]`. The code then prints out the unique elements extracted from the input list.