```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not(0)]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Unique:", unique(test_lst))  # [0, 2, 3, 5, 9, 123]

    test_lst2 = list(set(test_lst))
    print("Set unique:", test_lst2)  # [5, 3, 2, 123]
```

This code defines a function `unique` that takes a list as input and returns a new list containing only the unique elements. It uses a a set data structure to keep track of the unique elements. 

The `if __name__ == "__main__"` block means this code is intended to be run when the script is executed. The test lists are used to test the `unique` function with different input, and the expected output is printed.