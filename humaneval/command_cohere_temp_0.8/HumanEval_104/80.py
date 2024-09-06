```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This Python script defines a function `unique_digits` that takes a list of positive integers called `xs`. It employs a list comprehension to filter out elements that have at least one even digit, and then returns the sorted list of remaining elements. This behavior is illustrated in the provided example tests, where the function appropriately identifies and returns the expected values for both cases based on the given input list of positive integers `xs`.