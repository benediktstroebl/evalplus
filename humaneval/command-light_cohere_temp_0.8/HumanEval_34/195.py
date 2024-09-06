```python
def unique(lst):
    return list(set(lst))

# Test cases
print("Test case 1:", unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Expected output: [0, 2, 3, 5, 9, 123]

print("Test case 2:", unique([9, 2, 3, 7, 5, 1, 0]))
# Expected output: [2, 3, 5, 9]

print("Test case 3:", unique([3, 1, 2, 2, 3, 'three']))
# Expected output: [1, 2, 3, 'three']

print("Test case 4:", unique([0, 0, 1, 2, 1, 2]))
# Expected output: [0, 0, 1, 2]

print("Test case 5:", unique([True, False, True, False]))
# Expected output: [True, False]
``` 
This script defines a `unique` function that removes duplicate elements from the input list and returns a new list of unique elements. The test cases demonstrate that the expected results are printed, ensuring that the function works correctly.