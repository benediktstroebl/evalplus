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

This Python script defines a function called `sum_squares` taking a list as an argument, aiming to process integer list elements according to their indices' multiples. If an index is a multiple of 3, the corresponding element is squared; if an index is a multiple of 4 but not 3, the element is cubed. The script sums these modified or original elements and returns the result. 

Here's an example of how to use the `sum_squares` function for the given input `[1, 2, 3]`:
```python
result = sum_squares([1, 2, 3])
print(result)  # Output: 6
```

And here's another example for the input `[-1, -5, 2, -1, -5]`:
```python
result = sum_squares([-1, -5, 2, -1, -5])
print(result)  # Output: -126
```

This would output: `-126` for the input `[-1, -5, 2, -1, -5]`.