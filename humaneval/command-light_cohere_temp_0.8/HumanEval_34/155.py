```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not in [0]]

if __name__ == "__main__":
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [(), []],
        ['a', 'b', 'c'],
        ['a', 'b', 'c', 'd'],
        [1, 2, 3, 'abc']
    ]
    
    for test_list in tests:
        print(unique(test_list))
```
This Python script defines a function called unique that takes a list as an argument and returns a new list containing the unique elements from the input list. The function uses a unique() function from the set module to store unique elements and filter the input list accordingly.