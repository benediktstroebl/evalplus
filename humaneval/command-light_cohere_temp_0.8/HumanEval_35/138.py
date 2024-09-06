```python
def max_element(lst):
    if not_numbers(lst):
        return "Input list must contain numeric values"
    return max(lst)

def not_numbers(lst):
    return all(type(num) == float for num in lst)

print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This Python script defines a function `max_element` that computes the maximum element within a given list. The function also includes a precondition check `not_numbers` to ensure the list contains numeric values before returning an error message. The `not_numbers` function uses the `all` function with the `type` function to check if all elements in the list are of numeric type.