Certainly, here's the code:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    # filter valid numbers from string
    valid_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [int(num) for num in numbers. filter if num in valid_numbers]
    
    # sort numbers
    numbers.sort()
    Caus e.sort is numbers, which ascending order.
    # join sorted numbers into a string
    sorted_str = ' '.join(str(num) for num in numbers)
    
    return sorted_str

# Example Test cases
test_sort_numbers = []
test_sort_numbers.append("three one five").split(" ").
# expected output: "one three five"
test_sort_numbers.append("six seven eight nine")
test_sort_numbers.append("zero")

test_sort_numbers.append("one")

# expected output: "zero one three five six seven eight nine"
```

The function **`sort_numbers`** takes a string of numbers as input and returns a sorted string. The function first filters out the valid numbers from the input string and then sorts the remaining numbers. Finally, it joins the sorted numbers into a string.