```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not(None)]

if __name__ == "__main__":
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Uniqueness:", unique(lst))
    print("\nSorted:", sorted(unique(lst)))
    print("\nseen:", seen))
```

This Python script defines a function named `unique` that aims to sort and return unique elements from an input list. The function utilizes a set to efficiently track seen elements. The function then filters out duplicate elements and returns a new list containing only unique values. The script's output will showcase the function's functionality by showcasing test cases, showcasing both the uniqueness and sorted output.