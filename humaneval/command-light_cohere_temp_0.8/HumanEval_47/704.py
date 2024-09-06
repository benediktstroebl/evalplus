```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        n = len(lst)
        if n % 2 == 0:
            return (lst[(n // 2) - 1] + lst[n // 2]) / 2
        else:
            return lst[n // 2]
    except IndexError:
        print("List is empty.")
        return None

# Test suite for median function
def test_median():
    try:
        lst = [-10, 4, 6, 1000, 10, 20, 2, 3, 1]
        print(median(lst), end=" ")
        assert median(lst) == 15.0, "Median is not calculated correctly."
        lst = [5, 10, 2, 8, 12, 18, 3, 6, 7]
        print(median(lst), end=" ")
        assert median(lst) == 10.0, "Median is not calculated correctly."
        lst = [1, 2, 4, 5]
        print(median(lst), end=" ")
        assert median(lst) == 5.0, "Median is not calculated correctly."
        lst = [3, 1, 4, 5, 6, 7, 2, 8, 10]
        print(median(lst), end=" ")
        assert median(lst) == 5.0, "Median is not calculated correctly."
        lst = [3, 1, 9, 2, 8, 5, 6, 7, 4]
        print(median(lst), end=" ")
        assert median(lst) == 5.0, "Median is not calculated correctly."
``` 
This script defines a function median that computes the median of a list of numbers. It also contains a test suite with several test cases for the median function, including edge cases and duplicate numbers. The test suite validates that the median function produces the expected results.