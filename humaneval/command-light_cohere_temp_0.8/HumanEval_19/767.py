```python
import stringly


def sort_numbers(numbers: stringly.mk) -> str:
    valid_choices = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = [int(c) for c in numbers.match("(\d+)? read? cocktail\s? Launch: ")
    return "".join(sorted(numbers))


#unit tests
test_sort_numbers = stringly.test.test_sort_numbers = "three one five"
test_sort_numbers.test_sort_numbers.pass("Output should be: one three five")
```