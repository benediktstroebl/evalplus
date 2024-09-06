```python
def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    return min(odd, len(arr) - odd)
```

The function relies on the fact that an array is palindromic if and only if the number of odd elements is equal to the number of even elements. It also leverages the minimize the number of changes, one can change the odd elements to even ones or vice-versa. Hence the result is minimized by either being the `odd` value or `len(arr) - odd` value, whichever is minimum. 

The test cases are derived from the examples provided in the problem statement and are included in the python file along with the function for completeness. 

```python
test = [
    ([1,2,3,5,4,7,9,6], 4),
    ([1, 2, 3, 4, 3, 2, 2], 1),
    ([1, 2, 3, 2, 1], 0),
    ([], 0),
    ([1], 1),
    ([1, 2], 1),
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 3)
]

for arr, expected in test:
    result = smallest_change(arr)
    print(f'Input: {arr}, Expected: {expected}, Actual: {result}')
``` 

The test prints each test case, the expected value, and the actual value of the output from the `smallest_change` function.  This way, the code is fully self-contained and should run as soon as the script is opened.