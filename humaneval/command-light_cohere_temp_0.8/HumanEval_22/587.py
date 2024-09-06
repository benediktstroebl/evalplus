Here is a self-contained Python script that defines a function `filter_integers` that filters out non-integer values from a list, passing the test.
```python
def filter_integers(values):
    return [element for element in values if isinstance(element, int)]
```

This script provides a simple and clean way to filter a list of any values for integers, which is a common task in Python programming. It also ensures better code readability and maintainability by containing the logic within the function, making the main code clean and focused on its purpose.