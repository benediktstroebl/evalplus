```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine. Valid choices are re: {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
    return numbers.split().numbers.sort(numbers)make each the
         numbers=[int.isdigit(c) for c in numbers])
        if numbers == sorted(numbers):
            return numbers
    return "ERROR!"

# Example test cases
test_sort_numbers = []
test_sort_numbers.append("three one five")
test_sort_numbers.append("zero two three seven eight nine")
test_sort_numbers.append("one two three six four five")

def test_function(test_case: str) -> str:
    return sort_numbers(test_case)

for test in test_sort_numbers:
    print(test_function(test))
 ```