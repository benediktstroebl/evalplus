```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return "".join[num for num in numbers if num in "1234567890" else num].upper()
    """

test_sort_numbers = """
def test_sort_numbers():
    return sort_numbers("three one five")
"""

code = test_sort_numbers()
def main():
    assert code == "one three five"
    print("Test passed")

if __name__ == "__main__":
    main()
```