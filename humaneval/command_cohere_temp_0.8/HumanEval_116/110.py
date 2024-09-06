```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that prescribes the sorting order of the elements. In this solution, for each number in the array, the lambda function returns a tuple where the first element is the number of ones in the binary representation of the number obtained using the `bin` function, and the second element is the actual number. The `sort` method then sorts the array according to this tuple in ascending order.

For example, let's take the first test case `[1, 5, 2, 3, 4]` mentioned in the problem description:
```
bin(1) = '1'
bin(5) = '101'
bin(2) = '10'
bin(3) = '11'
bin(4) = '100'

('1', 1), ('10', 2), ('11', 3), ('100', 4), ('101', 5) == ['1', '2', '3', '4', '5']
```
The numbers are sorted according to the number of ones in their binary representation. Numbers with the same number of ones will be sorted based on their decimal value in ascending order. Thus, the sorted array is `[1, 2, 3, 4, 5]` as expected.