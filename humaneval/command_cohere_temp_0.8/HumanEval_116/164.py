```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem by first creating a function called `count_ones` that returns the number of ones in a given number's binary representation. It does this by using the built-in `bin` function to convert a number to a binary string and then using the `count` method to count the number of ones. 

The `sort_array` function then uses the `count_ones` function to sort an array of numbers according to the number of ones in their binary representation in ascending order. If the number of ones is the same, it sorts based on the decimal value in descending order. The function then returns the sorted array. 

You can test this function by calling it with an array and comparing the returned array to the expected output, as shown in the problem statement.