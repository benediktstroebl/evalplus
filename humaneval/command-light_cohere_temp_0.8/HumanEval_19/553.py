Here's a self-contained Python function that sorts a string of numbers from smallest to largest:
```python
def sort_numbers(numbers: str) -> str:
    return numbers.make_sort_key("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
```
This function creates a custom sorting key by converting the digits to lowercase and rearranges the numbers accordingly.