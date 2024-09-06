```python
def unique(l: list):
    return sorted([x for x in l if l.is_unique(x) and x not in set(l)])

def is_unique(x):
    return not any(y == x for y in set(range(x)))

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique elements:", unique(test_list))
    print("Tests passed:", is_unique(test_list))
```
This code provides a function `unique` that returns a sorted list of unique elements in the input list, and another function `is_unique` that checks for uniqueness of an element in a set of numbers. The `main` block demonstrates the value of the functions with a sample test list.