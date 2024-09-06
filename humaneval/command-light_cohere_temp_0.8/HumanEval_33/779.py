```python
def sort_third(lst):
    return lst if len(lst) <= 1 else [2] + sort_third([3, 6])

# Test cases
test_sort_third = [
    dict(zip(['input'], [
        [1, 2, 3], 
        [5, 6, 3, 4, 8, 9, 2],
    ])),
    assert sort_third([1, 2, 3]) == [1, 2, 3], "First test failed"
]

test_sort_third2 = [
    dict(zip(['input'], [
        [5, 6, 3, 4, 8, 9, 2], 
        [1, 2, 3, 7, 4, 8, 9],
    ])),
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5], "Second test failed"
]

# Main code
if __name__ == "__main__":
    print("First Test Passed:")
    test_sort_third.py()
```