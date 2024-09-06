```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem as described in the markdown code block. It first creates a function called `count_ones` that returns the number of ones in a binary representation of a given number. It then creates a function called `sort_array` that uses a lambda function to sort an array of numbers by first sorting them by the count of ones in their binary representation and then by their decimal value in the case of a tie. This ensures that the array is sorted according to the given specifications.