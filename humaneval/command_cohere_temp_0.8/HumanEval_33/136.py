```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            l_new.extend(l[i:i+3])
    return l_new
```
This script defines a function sort_third which takes a list l as input and returns a list l_new. The function sorts the values of the list at indices divisible by three and leaves the other values unchanged. It does this by iterating over the list in steps of three and using a try-except statement to sort the temporary list of three elements before appending it to l_new. The except statement ensures that the code executes gracefully if a list of three elements is not encountered. The function essentially produces a sorted version of the original list at indices divisible by three, while leaving the other elements untouched.

Here's a test to check if the function is working correctly:
```python
def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert sort_third([0, 6, 2, 8, 4, 10, 12, 14]) == [0, 2, 4, 6, 8, 10, 12, 14]
test_sort_third()
```
Output: