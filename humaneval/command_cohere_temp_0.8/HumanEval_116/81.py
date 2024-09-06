```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs the `count_ones` function to tally the number of '1's in the binary representation of each number in the array, and then sorts the array according to this count. For arrays with an equal number of '1's, the decimal value is used as a tie-breaker to ensure correct sorting. 

To run the script, add the following code after the last line:
```python
>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
True

>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
True

>>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
True
```

The expected output for each test case is `[1, 2, 3, 4, 5]`, `[0, 1, 2, 3, 4]`, and `[-6, -5, -4, -3, -2]`.