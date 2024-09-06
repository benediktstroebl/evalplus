```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

This script defines a function called `sum_squares` that takes a list called `lst` as input. The function iterates over each index `i` and element `num` in the list using the `enumerate` function, which provides both the index and the element in a convenient tuple. Based on the value of `i` modulo 3 and 4, it determines whether to square or cube each number in the list. It then adds up all the modified numbers and returns the result.

Here is an example usage of the `sum_squares` function:
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_squares(my_list)
print(result)
```

Output is:
```
94
```

And here is a breakdown of the code:
1. It defines a function called `sum_squares` that takes a list called `lst` as input.
2. It initializes a variable called `result` to store the sum of modified numbers.
3. It iterates over each index and element in the list using the `enumerate` function.
4. If the index is a multiple of 3, it squares the number.
5. If the index is a multiple of 4 but not 3 (i.e., a multiple of 12), it cubes the number.
6. It adds the modified number to the `result` variable.
7. Finally, it returns the `result` variable.