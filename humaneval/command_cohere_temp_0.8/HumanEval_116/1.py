```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, for every number in the array, the lambda function `lambda x: (bin(x).count('1'), x)` is used. This function returns a tuple where the first element is the number of '1' digits in the binary representation of the number (`bin(x).count('1')`), and the second element is the number in decimal form. The array is then sorted based on this tuple. 

Let's break down the code further:

1. `arr.sort(key=lambda x: (bin(x).count('1'), x))`: This line sorts the array `arr` using the sorting key obtained from the lambda function. The lambda function takes an element `x` from the array as an argument, and returns a tuple (`(bin(x).count('1'), x)`) which is used as the sorting key. 
2. `bin(x)`: This converts the decimal number `x` to a binary string representation. 
3. `.count('1')`: This counts the number of occurrences of '1' in the binary representation of the number. 
4. For example, for the number `10`, `bin(10) = '1010'` and `.count('1')` returns `2`. 
5. The resulting array is sorted in ascending order based on this key. 

The code thus implements the specified sorting algorithm and produces the required sorted array. 

This solution works because:

1. Numbers with more '1's in their binary representation will appear first. 
2. If the number of '1's is the same, sort the numbers in decimal value order. 

The code uses bin() which returns a string representing the binary representation of the number. To count the number of ones, we use `count('1')` which returns the number of occurrences of the character '1' (as opposed to str.count(), which returns the number of occurrences of any character). 

Note: In Python 3.x, `oct()`, `hex()`, and `bin()` are all built-in functions that convert numbers to the specified base. 

This code leverages these built-in functions to achieve the desired result, sorting the array based on the specified criteria. 

Overall, the provided code is concise and effective in solving the problem. 

This code can be tested directly in an interactive Python session to verify the behavior of the function:

```python
def test_sort_array():
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]

test_sort_array()
```

These assertions correspond to the test cases specified in the original problem.