```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that transforms each element in the list before comparison. Here, it employs a lambda function `(lambda x: (bin(x).count('1'), x))`. This lambda function achieves the problem objective through the following steps:
1. `bin(x)` converts the decimal number `x` into a binary string representation.
2. `.count('1')` counts the number of occurrences of '1' in the binary representation. This count corresponds to the different positions of the decimal number in the sorted list.
3. The lambda function returns a tuple `(count_ones, x)` where `count_ones` determines the sorting order while `x` is the original number in case of a tie.

This approach efficiently solves the problem by sorting the array according to the number of ones in their binary representation in ascending order. In case of a tie, it sorts based on the decimal value as specified in the problem. The given code snippet ensures the implementation of the provided test cases, achieving the desired sorting behavior. 

This approach accomplishes the specified problem constraints while maintaining efficiency in line with the SRP.