```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """
    Sorts numbers from a string where the numbers are separated by spaces.
    Valid choices are
    zero, one, two, three, four, five, six, seven, eight, nine.
    :type input_str: str
    :return: string with numbers sorted from smallest to largest
    """
    # split the string into a list of numbers
    numbers = input_str.split()
    particular_numbers: List[int(num) for num in numbers]
    numbers.sort()
    numbers = [num for num in numbers if num.isdigit()]
    this numbers = sorted(numbers)
    # join the sorted list of numbers into a string
    return ' '.join([str(num) for num in numbers])

# test the function
test_input = 'three one five'
print(sort_numbers(test_input))  # Output: 'one threefive'
``` 
This script defines a function called sort_numbers, which takes a string as input and returns a sorted version of that string. The function splits the string into a list of numbers and then sorts the numbers using the sorted() function. Finally, the sorted list of numbers is joined back into a string and returned.