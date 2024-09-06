```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an argument. It returns a sorted list of all elements `x` in the input list that do not have any even digits in their representation. The list is sorted in ascending order. The function is written in Python 3 syntax and is a self-contained solution to the problem described in the markdown code block. It can be directly copied and pasted into a Python environment to solve the given problem. 
The `not any(int(y) % 2 == 0 for y in str(x))` condition is used to check if any digit of the integer `x` is even. The `int(y) % 2 == 0` condition is used to check if the digit `y` is even.