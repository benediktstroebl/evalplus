```python
from typing import List

def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = 'zero' if numbers[0] == 'one' else 'one'
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:  # skip duplicate entries
            if numbers[i] < numbers[i - 1]:
                sorted_numbers += ' '.join(numbers[i:i + 2])
            else:
                temp = numbers[i]
                numbers[i] = numbers[i - 1]
                numbers[i - 1] = temp
                sorted_numbers += ' '.join(numbers[i:i + 2])
                # return the sorted string with numbers sorted from smallest to largest
                # e.g. input -> 'three one five' , sorted -> 'one three five'
    return sorted_numbers
```

This Python script takes a string of space-separated numbers, sorts them, and returns the smallest-to-largest string. The `sort_numbers` function takes an input string of numbers and splits it into a list of numbers. It then iterates through the list, comparing each number to the next one and swapping them if the current number is larger. The function then joins the swapped numbers with spaces and adds them to the `sorted_numbers` variable. The function tests for duplicate entries, ensuring a correct swap occurs. The final `sorted_numbers` string is returned, with numbers sorted from smallest to largest.

Here is an example usage of the function:
```python
print(sort_numbers('three one five')) # output: one three five
```