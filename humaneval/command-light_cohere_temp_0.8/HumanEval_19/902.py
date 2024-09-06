```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    thorough test suite for the numbers:
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    print(sort_numbers('six seven eight nine'))  # expected output: ['seven eight nine']
    print(sort_numbers('four five six'))  # expected output: ['five six'])
    print(sort_numbers('9002 one'))   # expected output: ['9002 one']
    print(sort_numbers(' Ninety-two'))  # expected output: ['Ninety-two']
    print(sort_numbers('three two'))    # expected output: ['two three']
    print(sort_numbers(' Ninety-Three'))  # expected output: ['Ninety-Three']
    print(sort_numbers('Zero123_456'))  # expected output: ['Zero123_456']
    print(sort_numbers('five six seven eight nine'))  # expected output: ['seven eight nine']
    ```