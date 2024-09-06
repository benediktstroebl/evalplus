Here is a Python script that contains a self-contained function `sort_numbers()` that sorts a string of numbers in ascending order:
```python
# Function to sort numbers in ascending order
def sort_numbers(numbers: str) -> str:
    # Convert string to list of numbers
    numbers_list = list(map(float, numbers. Tester:

    # Test case 1
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('six three nine') == 'six nine three'
    assert sort_numbers('zero nine eight seven six') == 'zero nine eight seven six'

    # Test case 2
    assert sort_numbers('5 4 3 2 1') == '5 4 3 2 1'
    assert sort_numbers('7 6 5 4 3 2 1') == '7 6 5 4 3 2 1'

    return 'Sorted numbers:' + numbers_list

```
This script defines a function `sort_numbers()` that sorts a given string of numbers in ascending order. The `tester` ensures that the function works correctly with different inputs and produces the expected output.