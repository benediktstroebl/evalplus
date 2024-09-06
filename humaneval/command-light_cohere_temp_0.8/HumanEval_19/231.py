```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 
    'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split() 
                        key = lambda x: x.sorted() 
                        return "".join()

# Test the function with a couple of inputs
test_list = ["three onefive", "zero two three eight", "six three seven nine"]
sorted_str = [x[0] for x in test_list.split()]
print(sorted_str)
```