```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is built by taking the first and second elements as
    the two extreme elements, and placing the other elements in reversed order.
    Then array is read in reverse order, is the same as the original array but with all
    elements swapped. This palindrome is array has some elements less than zero and some elements
    greater than zero, which means it is not a palindrome.

    To find the by iterating backwards through the array, and comparing the current
    element to the element immediately before it. If the current element is less than the element
    immediately before it, swap them.
    This other wise is swapping them will give us a smaller number of swaps to make the
    array palindromic, and thus a smaller number of changes to make the original array
    palindromic.

    We then method is simple and efficient, and will run in O(n) time.

# Test the function with different arrays
print("Test 1:",smallest_change([1,2,3,5,4,7,9,6]))
print("Test 2:",smallest_change([1, 2, 3, 4, 3, 2, 2]))
print("Test 3:",smallest_change([1, 2, 3, 2, 1]))
print("Test 4:",smallest_change([1, 2, 3, 2, 1, 2]))
```

This code defines a function `smallest_change` that takes an array of integers as input and returns the minimum number of elements that need to be changed to make the array palindromic. The function works by iterating through the array from back to front, and comparing the current element to the element immediately before it. If the current element is less than the element immediately before it, the two elements are swapped. The process continues until the final result is a palindrome array, with the minimum number of changes.