```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a given number's binary representation. It also defines the `sort_array` function, which sorts the array based on the number of ones in the binary representation in ascending order. If the number of ones is the same, it sorts them based on their decimal value in descending order. The code ensures that the given task is solved correctly by making the output consistent with the given expectations. Thus, the provided Python script solves the problem while adhering to the given guidelines.