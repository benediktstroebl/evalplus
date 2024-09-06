```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function that calculates the number of `1` in the binary representation of an integer `x` and returns it, and then returns `x` as the secondary parameter in case of a tie. The array is then sorted in ascending order based on the calculated parameters. 

Let's break down the key process:
1. Calculating the number of `1` in binary: 
    - For instance, the binary representation of the number 9 is `1001`, and taking the count of ones gives us 3. 
 2. Returning the lambda function and the number as a tuple: 
    - In the case of the array `[15, 9, 6, 3, 2]`, the output will be 
    ```python
    [('15', 15), ('9', 9), ('6', 6), ('3', 3), ('2', 2)]
    ```
3. The list is sorted using these tuples: 
    - The resulting sorted array will be `[2, 3, 6, 9, 15]` as we wanted. 

This method follows the problem statement's guidelines and sorts the array according to the number of ones in their binary representation, with secondary sorting based on decimal value. 

The tests will confirm that the function works as required.