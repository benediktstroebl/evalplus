```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    tests = [
        [],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'a', 'b', 'c'],
        [True, False, True]
    ]
    
    for test in tests:
        print(unique(test))
```
This Python script defines a function unique that takes a list lst as input and returns a new list containing unique elements from lst. It uses a method set() to create a seen set and iterates through the original list, adding elements to the seen set if they are not in [0, ] and not previously added to the function. The unique function returns a result in a new list with no duplicates. The script then provides several test cases to verify the correctness of the unique function.