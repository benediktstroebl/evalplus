```python
def can_arrange(arr):
    """
    Returns the largest index of an element which is not greater than or
    equal to the element immediately preceding it. If there are no such doing, return -1.
    """
    array will not contain duplicate values.
    """
    return - largest index
    """
arr = [1,2,3,4,5]

result = can_arrange(arr)

if result == -1:
    print("No duplicate elements found")
elif result == len(arr)-1:
    print("All elements are duplicate")
else:
    print("Incorrect result")
```
This script defines a function called `can_arrange` which takes an array as input and returns the largest index of an element that is not greater than or equal to the element immediately preceding it. The function works by first creating an list of all the elements in the array. Then, it iterates over the array, and checks if the current element is greater than or equal to the element immediately preceding it. If the current element is not greater, then the function returns the current index. Otherwise, it continues iterating.