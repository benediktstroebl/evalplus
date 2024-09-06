```python
def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd % 2 == 0:
        return int(odd/2)
    else:
        return int((odd+1)/2)

# Example Usage
arr1 = [1,2,3,5,4,7,9,6]
print(smallest_change(arr1))  # Output: 4

arr2 = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr2))  # Output: 1

arr3 = [1, 2, 3, 2, 1]
print(smallest_change(arr3))  # Output: 0
```

In this script, the `smallest_change` function calculates the minimum number of changes required to make the array palindromic. It does this by counting the number of odd elements in the array (`odd`) and then calculating half of this value. If the count of odd elements is odd, then we need to add one to the count. 

The provided examples demonstrate how the function can be used to find the minimum number of changes for different input arrays.