```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum([1 for i in range(len(arr)) if arr[i] != arr[-(i+1) % len(arr)]])
```

This function removes any duplicate elements within the array and then counts the number of elements that need to be changed to create a palindrome. The result is the number of elements that need to be changed in the least number of operations to create a palindrome. This is done by iterating through the array and counting the elements that are not symmetric with their index in reverse and dividing that number by 2 to get the minimum number of changes, which is always the floor of that number.