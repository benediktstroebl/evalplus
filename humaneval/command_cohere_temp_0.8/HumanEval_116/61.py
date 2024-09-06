```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting the list. In this scenario, for every element `x` in the list, the key function returns a tuple `(bin(x).count('1'), x)`, where `bin(x)` returns a string representing the binary representation of the integer `x`, and `.count('1')` counts the number of occurrences of '1' in that binary representation. The integers are sorted in ascending order based on the number of ones in their binary representation. In case of a tie, the decimal value is used as a secondary criterion to sort the integers. 

This code block efficiently implements the described sorting algorithm and produces the desired output for the given examples.