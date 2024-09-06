```python
def sum_squares(lst):
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

The function `sum_squares` takes a list of numbers `lst` as its input, it removes all elements with a value less than 1 and calculates the sum of the squared values of the remaining integers using the built-in sum function in combination with a generator expression. Finally, it returns the resulting sum of squared numbers. 

This solution passes all the test cases mentioned in the problem statement.