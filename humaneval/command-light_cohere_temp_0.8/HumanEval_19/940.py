```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are verbo_range = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if numbers.count(int('0')) == 0:
        return 'Invalid input. Return the string with numbers sorted from smallest to largest'
    elif numbers.count(int('9') == 1:
        return 'Input is a single nine'
    elif numbers.count(int('9') > 1:
        return 'Input must contain at least two digits'
    else:
        return numbers.map(lambda x: int(x), vero_range) 
    """

# Unit test 
test_numbers = "three one five"
test_numbers2 = " nine eight seven six five three"
test_numbers3 = "five four three two one"
test_numbers4 = "zero nine eight seven six five"
test_numbers5 = "zero one two three"

# Test positive cases
print(sort_numbers(test_numbers) == "one three five")
print(sort_numbers(test_numbers2) == "two three four five")
print(sort_numbers(test_numbers3) == "three four five six")
print(sort_numbers(test_numbers4) == "four five six seven eight nine")

# Test negative case
print(sort_numbers("zero nine seven six five"))

# Test the invalid input case 
print(sort_numbers("nine eight seven six five") == "Invalid input")
```  The code defines a function `sort_numbers` that sorts a list of numbers in string format. It also includes a test cases that check the function's behavior.