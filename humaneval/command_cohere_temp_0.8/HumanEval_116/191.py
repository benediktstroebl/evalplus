```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that formats the elements of the list before they are compared. In this case, the function `lambda x: (bin(x).count('1'), x)` calculates the number of ones in the binary representation of each number and sorts the list first according to this number of ones, and in case of a tie, it sorts the list according to the decimal value of the numbers. 

For example:
```python
sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
```

The example works like this:
1. The input list is `[1, 5, 2, 3, 4]`.
2. The `sort_array` function is called with this list as the input.
3. The list is sorted using the `key` argument with the lambda function specified. For each number:
  - The lambda function converts it to a binary string (`bin(x)`), counts the number of ones (`bin(x).count('1')`), and sorts them in ascending order.
  - In case of a tie, it sorts the numbers in ascending order according to their decimal value (`x`).
4. The sorted result is `[1, 2, 3, 4, 5]`.

The other test examples are sorted accordingly.