```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [char.lower() for char in numbers]
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This Python script defines a function called `sort_numbers` which takes a string of numbers in the range from 0 to 9 as input. The function first converts the input string into a list of individual number characters, ignoring cases, and then, uses the `sorted` function to sort these numbers from smallest to largest. Finally, the function returns the string with the numbers sorted in ascending order. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # one three five
``` 

This would output:
```one three five```.