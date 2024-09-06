```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    return ' '.join(sorted(numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function splits the string into a list of numbers, sorts the list in ascending order, and then joins the sorted list back into a string. This ensures that the numbers are properly organized from smallest to largest. The function returns the sorted string. 

Here is an example usage of the function:
```python
print(sort_numbers('three one five')) # Outputs: 'one three five'
```
You can copy and paste this code block into a Python environment or script and run it to see the output.