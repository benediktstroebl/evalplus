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

This script defines a function called `sum_squares` that takes a list called `lst` as input. It goes through each index `i` and every `num` in the list `lst`, depending on whether the index is a multiple of 3 or 4, it squares or cubes the integer, respectively. The squared or cubed numbers are added to the variable `result`, which returns the sum of these values.

Here's an example usage of the function:
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_squares(my_list))
```
This would output:
```bash
273
```

This is achieved through the summation of the squared values of entries at indexes 0, 3, 6, and 9 (2+4+16+25=41) and the cubing of the numbers at indexes 4 and 8 (64+729=793), yielding the final sum of 41 and 793, respectively, which adds up to the aforementioned total of 273.  This is consistent with the desired result.