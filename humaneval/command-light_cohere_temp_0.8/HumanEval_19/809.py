```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers. belts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = numbers.split()
    valid = False
    for n in numbers:
        if n in belts:
            valid = True
            break
    if valid:
        numbers.sort()
    return " ". ".join(numbers)
    else:
        return "Invalid input"

# Unit tests
def test_sort_numbers():
    test_data = {
        "three one five" : "one three five"
    }
    for data, expected in test_data.
    actual = sort_numbers(data)
    print(f"Data: {data} Expected: {expected}, Actual: {actual}")
    return actual == expected
```