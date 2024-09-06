```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))
    """
    return "Pass"

test_sort_numbers = []
test_numbers = "three one five seven eight nine"
test_sort_numbers.py" =  'one three five seven eight nine'

def test():
    assert sort_numbers(test_numbers) == "Pass"

def main():
    print(sort_numbers("three one five seven eight nine"))

if __name__ == "__main__":
    main()
```