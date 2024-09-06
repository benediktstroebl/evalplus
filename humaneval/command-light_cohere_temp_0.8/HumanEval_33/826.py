```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) // 3 if x % 3 == 0 else x)

# Unit tests
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

if __name__ == "__main__":
    test_sort_third()
```
This code defines a function sort_third that sorts a list using the key function. It also has a test_sort_third(), which contains unit tests to verify the correctness of the sort_third function. This code is a way is self-contained and can be used standalone.