```python
from typing import List

# Create a dictionary mapping number words to their integer equivalents
num_to_int = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Convert the number words to integers, sort them, and convert back to number words
    sorted_num_list = [num for _, num in sorted(zip([num_to_int[num] for num in num_list], num_list))]

    # Join the sorted number words back into a string and return
    return''.join(sorted_num_list)

# Test the function
print(sort_numbers('three one five'))  # 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero')) 
# 'zero one two three four five six seven eight nine'
```