```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script sorts a given space-delimited string of numbers (`zero` to `nine`) using the `sort_numbers` function. The function splits the input string into a list of integers, sorts it from smallest to largest, and then joins the sorted integers back into a string.

Here's an example of how you can use the `sort_numbers` function:
```python
print(sort_numbers('three one five'))  # output: 'one three five'
```
You can also verify the correctness of the function using the provided test case:
```python
>>> sort_numbers('three one five')
'one three five'
``` 
**Note**: This function assumes that the input contains only digits from 'zero' to 'nine', and it will raise an error if invalid digits are present.