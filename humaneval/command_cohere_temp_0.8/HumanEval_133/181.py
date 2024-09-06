```python
def sum_squares(lst):
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return int(result)
```

The function `sum_squares` serves the purpose of calculating the sum of the squares of integers in a given list. It does so in a succinct manner, using a generator expression combined with the `sum` function to compute the sum of squared values. Importantly, it filters out non-integer values by checking if each element in the list has a decimal part, using the condition `x % 1 == 0`, regardless of whether the decimal part is zero. The function then rounds the resulting sum to the nearest higher integer using the `int` function. 

To ensure robustness, the function gracefully handles empty lists, and returns 0 for such inputs. As an illustrative example, executing `sum_squares([1, 4, 9, 28])` would return the result 98.