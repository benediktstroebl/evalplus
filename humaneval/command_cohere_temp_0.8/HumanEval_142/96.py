```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an argument. It goes through each entry in the list and squares it if the index is a multiple of 3, and cubes it if the index is a multiple of 4 but not 3. It then returns the sum of these modified entries. The behavior is specified by the provided examples that are included in the function specification. Such a behavior is easily comprehensible once it is known that the sum of squared integers, cubes of integers and the sum of an integer and its cube are acquainted with each other:
- The sum of squares of integers behaves like **n^2** for some integer n,
- The sum of cubes of integers behaves like **n^3** for some integer n,
- The sum of an integer and its cube behaves like **n + n^3** for some integer n.

Hence, applying these known behaviors to the function specification leads to the following summation:
`sum(num ** 2 for num in lst if i % 3 == 0) + sum(num ** 3 for num in lst if i % 4 == 0 and i % 3 != 0)`

Which exactly corresponds to the summation performed by the above code.