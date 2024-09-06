```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2
    else:
        return lst[len(lst)//2]

# Unit tests
def test_median():
    try:
        test_lst = [-10, 4, 6, 1000, 10, 20, 1, 2, 4]
        assert median(test_lst) == 15.0
        except:
            raise AssertionError("Median does not work as expected")

# Example usage
if __name__ == "__main__":
    test_median()
```
This Python code defines a function `median` that calculates the median value of a given list `lst`. It also includes a test function `test_median` with a sample list and corresponding assertion. The `main` block demonstrates the usage of the `median` function with an example list, and the test function is called to validate the correctness of the median calculation.