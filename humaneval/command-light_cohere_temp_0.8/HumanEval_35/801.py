```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test the function with different lists
if __name__ == "__main__":
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst1) == 123

    lst2 = [-5, 3, -20 [], 1, 2, 4]
    assert max_element(lst2) == 4

    lst3 = [1, 2, 3, -5, -6]
    assert max_element(lst3) == -5
```
The function `max_element` takes a list `lst` as an argument and returns the maximum element in that list using the `max()` built-in function. 
Test the function using sample lists and make sure that the result is correct.

Please note that this code is self-contained and does not require any additional imports or external functions.