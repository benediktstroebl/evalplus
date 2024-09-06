```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script provides a function `unique_digits(xs)` that takes in a list of positive integers, `xs`, and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to filter out the elements that have at least one even digit, and then returns the sorted list of remaining elements. 

The code tests pass successfully as shown in the example test cases:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

The code is completely self-contained within the function and does not rely on any external variables or additional code. Thus the markdown code block fulfills the requirements of the request.