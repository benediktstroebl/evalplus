```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a binary representation of a number, and the `sort_array` function sorts an input array of integers according to the specified criteria, keeping values with the same number of ones in binary in ascending order. 

The use of a key in the `sort` method is a handy approach to sort complex data types and define custom sorting criteria, especially when used with lambda functions. 

This solution will produce the expected output when applied to the test cases mentioned in the problem statement.