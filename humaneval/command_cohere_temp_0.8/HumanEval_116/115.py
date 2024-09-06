```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The code defines a Python function `sort_array` that takes an array of non-negative integers as input. It sorts the array according to the number of ones in their binary representation. If the number of ones is the same, it sorts them based on their decimal value in descending order. The function meets the provided test cases, ensuring the output is correctly sorted.  This algorithm operates by first generating a count of "1" digits in the binary representation for each number using the `count_ones` helper function. Subsequently, it employs a sorting key that combines the calculated one-counts in ascending order and uses the decimal value in descending order as a secondary sorting criteria for tiebreakers.