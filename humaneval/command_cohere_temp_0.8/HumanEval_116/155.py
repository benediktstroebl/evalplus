```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array. The `sort_array` function then uses a lambda to sort the array by first organizing elements with the same number of ones in their binary representation in ascending order and then sorting the remaining elements in descending order of their absolute value. The resulting sorted array meets the expectations stated in the problem description. You can use this code to solve the problem and achieve the intended behavior.