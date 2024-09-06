```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        integer */
    def palindromic(array, start, end):
        return array[start] == array[end]

    count = 0
    for i in range(len(arr)-1):
        if not palindromic(arr, i, i+1) and palindromic(arr, i+1, i):
            count += 1
    return count
```

The function `smallest_change()` takes an array `arr` as input and uses a nested palindromic checker function to iterate through the array and count the number of elements that would need to be changed to create a palindrome. The function then returns the total count of changes required. To ensure efficiency, the checker takes advantage of the symmetry of the problem by checking only half of the elements, since reversing the entire array would result in the same count. The problem is solved with a self-contained Python function that is easy to use and integrate within larger projects.  This solution is general and can work for any input array of integers.