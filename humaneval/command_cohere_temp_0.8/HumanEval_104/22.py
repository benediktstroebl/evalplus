```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the prompt. It takes a list of positive integers `xs` as input and returns a sorted list of all elements that do not contain any even digits. The function uses a list comprehension to filter out elements that have at least one odd digit, and then sorts the resulting list in increasing order.

Here's an example of how you can use this function with the examples provided in the prompt:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```
This would return the expected outputs for the given examples, sorting the result list in increasing order as requested.