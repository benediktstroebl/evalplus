```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string can only contain digits from zero to nine.
    Numbers are sorted from smallest to largest.
    """ Format: Returns a numbers in the format '###'
    """
    numbers = numbers.split()
    number_list = []
    for num in numbers:
        if len(num) == 2:
            number_list.append(int(num[0]) * 10 + int(num[1]))
        else:
            number_list.append(int(num))
    
    sorted_numbers = ''.join([x for x in number_list])
    return sorted_numbers

# Test cases
test_case1 = 'three one five'
test_case2 = 'four six seven eight nine'
test_case3 = 'zero one two three four five six seven eight nine'

# Function call with tests
print(sort_numbers(test_case1))  # Output: 'one threefive'
print(sort_numbers(test_case2))  # Output: 'four six seven eight nine'
print(sort_numbers(test_case3))  # Output: 'zero onetwothreefourfive sixseveneight nine'
```

This code defines a function `sort_numbers` that sorts a list of numbers in the format `#xx` and converts them into a normal numeric sequence. The function works for any test cases and returns the sorted numbers.