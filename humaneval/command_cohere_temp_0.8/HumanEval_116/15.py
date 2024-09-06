```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script uses the `count_ones` helper function to determine the number of ones in the binary representation of each element in the array. It then sorts the array using a custom key function that first compares the number of ones in the binary representation in ascending order and then compares the decimal value in the event of a tie. The resulting sorted array meets the specified conditions for the problem. You can verify this by running the code and checking if the output is as expected. You can use this code to efficiently solve this specific problem.