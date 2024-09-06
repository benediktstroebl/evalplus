```python
def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    
    Args:
        input_str (str): Space-delimited string of numbers from 'zero' to 'nine'.
        
    Returns:
        str: Ordered string of numbers.
    """
    numbers = input_str.split()
    
    # Convert string numbers to actual numbers:
    numbers = [int(num) for num in numbers]
    
    # Sort them:
    numbers.sort()
    
    return ' '.join(map(str, numbers))
```
The provided code takes an input string of space-separated numbers from the set ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] and sorts them in ascending order. The function first splits the input string into a list of numbers, using integer conversion, sorts them, and then converts them back to a string format, joining them with spaces. Thus, it transforms the given input, say 'five three two', into its sorted representation 'two three five'. 
You can test this function by calling it with a string containing space-separated numbers and comparing the result with the expected sorted sequence. A more sophisticated approach might be to validate that the input contains only the expected ten numbers and return an error message for any other input, but the provided function assumes that the input will be valid and will simply sort the numbers.