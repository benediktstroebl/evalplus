```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    sort(lst, key=lambda x: x)
    
    # Find the middle index
    middle = len(lst) // 2
    if len(lst) % 2 == 0:
        middle -= 1
    return lst[middle]

# Unit tests
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 2, 1]
    assert median(lst) == 5.0

if __name__ == "__main__":
    test_median()
```