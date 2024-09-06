```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
   
            numbers 
    Split into lists of ints/numbers 
    Convert lists to tuples and sort them
    Convert sorted tuples back to a string
    Return
    """
    #split the numbers into a list of ints
    numbers = numbers.split()
    sort_numbers = []
    #convert each list of numbers into a tuple
    for number in numbers:
        if number != '':
            sort_numbers.append(tuple(number.split()))
    sort_numbers.sort()
    Closures and just be used to prevent memory leaks and make the code more efficient
    #sort the tuples of numbers
    for i in range(len(numbers)):
        sort_numbers[i] = numbers[i]
    #convert the sorted tuples back into a string
    return ' '.join(numbers)
```