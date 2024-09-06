```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem as described in the markdown code block. It first creates a function called `count_ones` that returns the number of ones in a given number's binary representation. Then it creates the `sort_array` function, which sorts the array according to the number of ones in their binary representation in ascending order. If there is a tie, it sorts based on the decimal value in descending order. The script passes the test cases outlined in the code block and returns the expected output.