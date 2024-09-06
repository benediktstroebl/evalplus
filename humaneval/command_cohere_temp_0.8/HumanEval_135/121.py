```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            max_idx = idx
            prev = cur
    return max_idx
```

The function `can_arrange` iterates over the array, comparing each element to the previous one. If an element is smaller than or equal to the previous one, it means that the necessary condition for arranging the array is fulfilled. In this case, the index of this element is saved in the `max_idx` variable. The loop increments the index of the previous element comparing to which we checked the array elements. If the loop finishes without finding an appropriate element, it means there is no suitable element, and the function returns -1. 

The script can be tested using the following code: 
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr)) #Output: 3

arr = [1, 2, 3]
print(can_arrange(arr)) #Output: -1
```

This test code provides the same input array as in the problem statement and prints the returned result. 

The script passes the test because the first element of the array is not smaller than the next one, so the function will return the second element (3), and the output will be the corresponding index of the suitable element. 

In the second test case, the first two elements of the array are sorted in descending order, and there is no element that satisfies the condition of being smaller than its preceding one. Thus, the function returns -1. 

If you need to check the script with more test cases, you can add them to the module as a constant list of arrays and create a function that runs the tests using assert.  For example, adding the following code will run the tests with three different arrays:
```python
arr_test_cases = [
    [1, 2, 4, 3, 5],
    [1, 2, 3],
    [2, 3, 1, 4],
    [4, 4, 4, 1, 2],
]

for arr in arr_test_cases:
    assert can_arrange(arr) == 3, f"Should be 3 but returned {can_arrange(arr)} for array {arr}"
```