Here's a Python script that solves the problem:

```python
# Define a dictionary to map words to numbers
number_map = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    :param numbers: Input string of space-delimited numbers
    :return: Sorted string of numbers
    """
    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Map the words to numbers
    num_list = [number_map[num] for num in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Map the numbers back to words
    num_list = [list(number_map.keys())[list(number_map.values()).index(num)] for num in num_list]

    # Join the sorted list back into a string
    sorted_numbers =''.join(num_list)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five')) # Output: one three five
```

This script uses a dictionary to map the word representations of numbers to their numerical values. It then splits the input string into a list of numbers, maps the words to numbers, sorts the list, maps the numbers back to words, and finally joins the sorted list back into a string.