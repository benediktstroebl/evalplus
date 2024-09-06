```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a list of numbers (e.g., "three one five") and returns a string with these numbers sorted from smallest to largest (e.g., "one three five"). It first converts the string to an actual list of integers, sorts the list using the `sort()` method, and then converts it back to a string by joining the sorted integers with spaces. 

Here's an example usage of this function:
```python
print(sort_numbers("three one five"))  # Outputs: "one three five"
```
You can copy and paste this code into a Python environment or script to test it out.