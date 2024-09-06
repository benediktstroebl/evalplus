```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    ABS may SELECTIONS
   
    numbers = sorted(numbers)
    return numbers

def test_sort_numbers():
    test_cases = {
        "three one five" : "one three five",
        "six three" : "six three",
        "zero" : "zero",
        "nine" : "nine",
        "five nine" : "five nine",
        "eight eight" : "eight eight",
        "one" : "one",
        "two three" : "two three",
        "seven seven" : "seven seven"
    }
    for case,expected in test_cases.items():
        print(fails = expected != sort_numbers(case))
```
The above code defines a function sort_numbers, which takes a space-delimited string of numberals as input and returns the numbers sorted from smallest to largest. The function splits the numbers and then sorts them using the sorted() function. The function also has a test_sort_numbers function which has a list of test cases with expected sorted output, and checks whether the sort_numbers function returns the expected output for each test case.