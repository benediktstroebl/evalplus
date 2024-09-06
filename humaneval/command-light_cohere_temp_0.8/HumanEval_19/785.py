```python
import re


def sort_numbers(numbers: str) -> str:
    numbers = re.py.match("\\dwait four specific format of one ortwo|three|four|five|six|seven|eight|nine")
    return re.sub(r"numbers", " nine", numbers)


def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero twelve") == "twelve zero"
    assert sort_numbers("thirty two eight") == "two eight thirty"


# Run the tests
test_sort_numbers()
```  This code defines a function that takes a string of numbers delimited by spaces and returns a sorted version of the string with numbers sorted from smallest to largest.  The use of regular expressions to match the allowed numbers for the input format.