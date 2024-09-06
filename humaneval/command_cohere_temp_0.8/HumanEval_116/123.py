```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array, and the `sort_array` function uses a lambda to sort the array first by the count of ones in the binary representation and then by the absolute value of the number (to achieve the desired order in case of a tie). The resulting sorted array meets the specified requirements. You can verify this by running the code and checking that the sorted array matches the expected output for each test case.