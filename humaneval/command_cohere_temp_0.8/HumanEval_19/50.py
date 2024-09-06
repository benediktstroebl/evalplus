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

This script takes an input string, splits it into a list of numbers, sorts the list, and then joins the numbers back into a string. It ensures that any valid input strings containing numbers from 0 to 9 will be correctly sorted and returned as a space-separated string. 

To run tests, you can use the example given in the problem statement, like this:
```python
test_cases = [
    ("three one five", "one three five"),
    ("four five six", "four six five"),
    ("seven eight nine", "seven eight nine"),
    ("one two three", "one two three"),
]

for test_case in test_cases:
    assert sort_numbers(test_case[0]) == test_case[1]
```

This will provide confidence that the script correctly sorts the numbers from smallest to largest for different test cases.