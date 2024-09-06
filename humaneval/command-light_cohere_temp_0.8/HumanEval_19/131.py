Here is a self-contained Python script that defines a function sort_numbers that sorts a string of numbers from zero to

```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sorted()

# convert list of numbers into string
numbers = list(map(str, numbers. numbers)))
# use the sorted() function to sort the numbers in ascending order
sorted_numbers = sorted(numbers)
# join the sorted numbers back into a string
return ''.join + ''.join(sorted_numbers)

if __name__ == '__main__':
    unittest.TestCase(). org.ns using of. mainline for the  test if sort_numbers('three one five') == 'one three five'
    unittest.TestCase.main()
 simple_numbers('three one five') == 'one three five'
    # pass additional tests
```