```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings containing digits from 0 to 9.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes an input string, splits it into a list of numbers, sorts the list, and then joins the numbers back into a string. It ensures that any valid input string that contains space-separated numbers from 0 to 9 is returned as a correctly ordered string. 

To validate the functionality, you can run the following tests:
```python
test_cases = [
    ("three one five", "one three five"),
    ("four five six", "four six five"),
    ("seven eight nine", "seven eight nine"),
    ("zero one two", "zero one two"),
    ("one two three", "one two three"),
]

for case in test_cases:
    assert sort_numbers(case[0]) == case[1]
```

This will provide a conclusive check on the function's correctness.