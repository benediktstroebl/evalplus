```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem as described in the prompt. It defines a `count_ones` function to calculate the number of ones in a binary representation, and the `sort_array` function sorts the array using a lambda function that leverages `count_ones` to sort according to the specified criteria. The function then returns the expected sorted array.