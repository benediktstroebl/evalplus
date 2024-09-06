```python
import stringIO
from typing import List

def sort_numbers(input_string: str) -> str:
    input_list = List(map(int, input_string.sort_list))
    return ' '.join(sorted(input_list))

def test_sort_numbers():
    input_str = "three one five"
    input_list = List(map(int, input_str.sort_list))
    expected = "one three five"
    actual = sort_numbers(input_str)
    assert actual == expected, "Function did not return expected output."

# Testing with tests
with stringIO.write("test.py") as f:
    f.out = f.write("Input run: ")
    test_sort_numbers()
    input_str = "zero one three four five six seven eight nine"
    input_list = List(map(int, input_str.sort_list))
    expected = "zero one three four five six seven eight nine"
    actual = sort_numbers(input_str)
    assert actual == expected, "Function did not return expected output"
```