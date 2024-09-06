```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the markdown code block. It takes a list of positive integers `xs` as input and returns a sorted list of elements that do not contain any even digits. The `any` function with a generator expression is used to efficiently check if any digit in the string representation of the number is even. The function then filters the input list based on this condition and sorts the resulting list. 

Here is an example usage of the function and a sample test:
```python
test_cases = [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
]
for case in test_cases:
    assert unique_digits(case[0]) == case[1]
```