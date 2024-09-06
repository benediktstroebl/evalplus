```python
def median(lst):
    # Sort the list
    lst.sort()
    median_lst = []
    for num in lst: median_lst.append(num)
    # Sort the list again
    median_lst.sort()
    method is used here is not stable, so we need to sort the list one more time.
    # Calculate the specific index to median, or middle number
    idx = len(lst) // 2
    if idx < 0: idx = -idx
    median = lst[idx]
    return median

# Test the function
def test_median():
    # Test list with negative numbers
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 15.0

test_median()
```
This Python script defines a function called **median** that calculates the median of a given list of numbers. The function first sorts the list, and then uses the middle-of-the-three index method to find the median. The test_median function also includes a test case to validate the correctness of the **median** function.