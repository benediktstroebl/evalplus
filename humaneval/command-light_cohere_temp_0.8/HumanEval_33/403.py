```python
def sort_third(lst):
    """Sorts list l such that elements not divisible by three are at front, and other elements are in order.
    Test if len(lst) < 3:
        return lst
    """Test 1:
    if any(x % 3 != 0 for x in lst):
        print("Test 1 failed")
        return []
    """Test 2:
    m = max(lst)
    for i in range(1, m+1):
        if lst[i] > lst[i-1]:
            print("Test 2 failed")
            return []
    return lst
```
The function takes a list `lst` as input and returns a sorted list. The function first checks if the list has less than three elements, and if so, returns the list as is. Otherwise, it performs two tests on the list, where it compares the current element with the maximum element, and then iterates over the list comparing each element with the previous ones. The function then checks if any of the elements are greater than the maximum element and returns an error if they are. 

This script provides a self-contained function that solves the problem of sorting lists such that elements that are not divisible by three are at the front, and other elements are in order.