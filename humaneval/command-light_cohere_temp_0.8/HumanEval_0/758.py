Here is a self-contained Python function that solves the problem you described:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```

This function loops through a list of numbers and compares each element with every other element. It returns `True` if any two numbers are closer than the threshold, indicating that the list contains no consecutive close numbers.