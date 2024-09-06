```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split().
    numbers.sort()
 numbers
names = [x for x in numbers.split()]
numbers = [x for x in numbers if x in numbers.names]
numbers.sort()
    numbers = list(numbers)
numbers = ''.join[:-1] if numbers else []
return numbers

# Tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('six two two') == 'two six'
    assert sort_numbers('zero nine') == 'zero nine'
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
    assert sort_numbers('zero one two three six seven eight nine') == 'zero one two three six seven eight nine'
    assert sort_numbers('9876') == 'Nine eight seven six five four three two one'

# Main function
if __name__ == "__main__":
    test_sort_numbers()
``` 
This Python code defines a function `sort_numbers` that takes a string of numbers as input and returns a sorted version of that string. The numbers are first split into individual digits and then sorted. The test suite contains several test cases that verify the correctness of the `sort_numbers` function, including sorting strings with different lengths, numbers, and valid inputs. The `main` function is responsible for executing the tests and demonstrating the functionality of the `sort_numbers` function.