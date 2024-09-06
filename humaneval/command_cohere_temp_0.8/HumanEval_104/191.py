```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the prompt. It takes a list of positive integers `xs` as input and returns a sorted list of all elements that do not contain any even digits. The function uses a list comprehension to filter out elements that have at least one odd digit, and then sorts the resulting list in increasing order.  The behaviour is demonstrated by the provided examples.