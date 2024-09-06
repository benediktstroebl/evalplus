```python
def sort_even(lst):
    """This function sorts the list lst such that all even indices are equal, and the list is sorted overall."""
    return sorted(lst,key=lambda x: x if x%2==0 else x-1)

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [7, 8, 9]
]

def test_sort_even():
    """This function tests the sort_even function using the test cases."""
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([7, 8, 9]) == [7, 8, 9]

# Main function
if __name__ == "__main__":
    test_sort_even()
```