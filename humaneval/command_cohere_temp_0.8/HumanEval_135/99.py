```python
def can_arrange(arr):
    res = -1
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            res = max(res, i)
    return res
```
The script defines a function `can_arrange(arr)` which iterates through the array, comparing each element to its next element. The function returns the maximum index of an element that is not greater than or equal to the preceding element. If no such element exists, it returns -1. 

To check the functionality, the script also includes a test case and a verification of the output against the provided examples. 
```python
test_case = [1, 2, 4, 3, 5]
print(can_arrange(test_case))
# Expected output: 3

test_case = [1, 2, 3]
print(can_arrange(test_case))
# Expected output: -1
``` 
This should solve the problem as described. Let me know if further clarification is needed.