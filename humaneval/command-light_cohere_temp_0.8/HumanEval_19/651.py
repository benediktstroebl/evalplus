Here's the self-contained Python script with a function that solves the problem of sorting numbers in Markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Convert string to list
    numbers = [int(num) for num in numbers.
    # Sort theired numbers list
   
    # Convert back to string
    sorted_numbers = ''.join(sorted(numbers))
    return sorted_numbers

# Unit tests
def test_sort_numbers():
    # Input string
    numbers = "three one five"

    # Call the function
    sorted_num = sort_numbers(numbers)

    # Compare with expected output
    expected = "one three five"
    assert sorted_num == expected, "Function does not sort correctly."

if __name__ == "__main__":
    test_sort_numbers()
```

In this code, we have a function `sort_numbers` that takes a string of numbers and returns them sorted from smallest to largest. The function works by converting the string of numbers into a list, then sorting the list, and finally converting the sorted list back into a string. The unit tests function checks if the function is working correctly by comparing the output with the expected output.