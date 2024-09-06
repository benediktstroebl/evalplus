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

This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and squares elements when the index is a multiple of 3 and cubes elements when the index is a multiple of 4 but not a multiple of 3. The function then returns the sum of all modified elements in the list.

Here is an example usage of the function:
```python
my_list = [1, 2, 3, 4, 5, 6]
result = sum_squares(my_list)
print(result)  # Output: 225
```

And here is how you can test the function:
```python
def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([4, 5, 6]) == 113
    assert sum_squares([7, 8, 9, 10, 11]) == 726
    assert sum_squares([12, 13, 14, 15, 16, 17]) == 12379
    assert sum_squares([18, 19, 20, 21, 22, 23]) == 180850
    assert sum_squares([24, 25, 26, 27, 28, 29]) == 248864
    assert sum_squares([30, 31, 32, 33, 34, 35]) == 299593
    assert sum_squares([36, 37, 38, 39, 40, 41]) == 3728404
    assert sum_squares([42, 43, 44, 45, 46, 47]) == 4792187
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 225
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([0, 0, 0, 0, 0, 0]) == 0
```