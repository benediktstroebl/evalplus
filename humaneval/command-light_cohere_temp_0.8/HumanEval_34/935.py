```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ] and x]

if __name__ == "__main__":
    test_lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    unique(test_lst)
    print("Test succeeded.")
```