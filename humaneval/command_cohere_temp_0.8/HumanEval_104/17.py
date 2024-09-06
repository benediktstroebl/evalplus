```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script defines a function `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list using a list comprehension to include only those integers whose digits are all odd (i.e., not any even digit). The list is then sorted in increasing order and returned.

The `not any()` is used to negate the `any()` test result, ensuring that only integers with all-odd digits are included. This is a more concise and efficient way to achieve the goal compared to using `if not x or int(y) % 2 != 0 for y in str(x)` as in the example in the previous response.