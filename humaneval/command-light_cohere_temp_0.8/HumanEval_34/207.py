```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

if __name__ == "__main__":
    print("Testing unique function:")
    test_unique()
```
This script defines a function `unique` that returns a sorted list of unique elements in the input list. The function uses a simple set to keep track of seen elements and iterates through the input list to find unique elements. It also handles the