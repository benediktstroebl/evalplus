Certainly! This is a self-contained function that sorts a list of numbers in markdown code block:
```python
def sort_numbers(numbers: str) -> str:
    # convert string to list of numbers
    numbers = list(map(int, numbers. new))  # sort the performed list
    # create a string from the sorted numbers
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```