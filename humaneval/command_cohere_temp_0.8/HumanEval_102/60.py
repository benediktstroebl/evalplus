```python
def choose_num(x, y):
    max_even = (x + y) // 2
    min_even = max(x, y) // 2
    if max_even >= min_even and max_even % 2 == 0:
        return max_even
    elif max_even < min_even or max_even % 2 != 0:
        return -1
```

The function takes two positive numbers `x` and `y` as inputs and first calculates the middle value between `x` and `y` (`(x + y) // 2`) and stores it in the variable `max_even`. Then it calculates the minimum even number within the range of `x` and `y` inclusive, which is half of the maximum value between `x` and `y` and stores it in the variable `min_even`. Then it checks if the `max_even` is greater or equal to `min_even` and if it is an even number, in both conditions being true it returns `max_even` as it is the biggest even number within the range, otherwise it returns `-1` if either condition is false. 

Here's a breakdown of the conditions: 
- `max_even >= min_even`: This condition checks if the middle number is greater than or equal to the minimum even number. This is possible only if the range of x and y contains at least one even number.
- `max_even % 2 == 0`: This condition checks if the middle number is even. This is necessary to ensure that the "biggest even number" criterion is met.

The code will return -1 if the middle number is less than the minimum even number, or if the middle number is odd. In these cases, there are no even numbers in the specified range.