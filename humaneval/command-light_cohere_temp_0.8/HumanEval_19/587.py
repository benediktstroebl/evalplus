```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are
    numbers = list(map(int, numbers. }

    numbers = sorted(numbers, reverse = True)
    return ' '.join(numbers)

# Tests
test_sort_numbers = []
test_sort_numbers.append("zero")
test_sort_numbers.append("two")
test_sort_numbers.append("three")
test_sort_numbers.append("four")
test_sort_numbers.append("five")
test_sort_numbers.append("six")
test_sort_numbers.append("seven")
test_sort_numbers.append("eight")
test_sort_numbers.append("nine")

print("Test results:")
for n, exp in zip(test_sort_numbers, [sort_numbers(n) for n in exp])):
    print(exp, f"{n} is {exp}")
```