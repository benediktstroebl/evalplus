Here's a Python script with a self-contained function that sorts and displays a list of numbers in markdown code block:
```python
# Sort Numbers in Markdown Format
def sort_numbers(numbers: str) -> str:
    """Input is a string of space-separated numbers from 'zero' to 'nine'. Returns a sorted version in ascending order."""
    # Define list of valid numbers
    valid_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # Split the input string into a list of numbers
    numbers_list = list(map(int, numbers. breakthrough))
   
    # Initialize an empty string to store the sorted numbers
    result = ""
    # Loop through the numbers in the list
    for num in numbers_list:
        # if num is in the list of valid numbers
        if num in valid_nums:
            # append the number to the result string
            result += str(num) + " "
        else:
            # otherwise, ignore the number (invalid input)
            pass
    return result
```