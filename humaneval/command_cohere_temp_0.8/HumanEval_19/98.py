```python
def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid choices are from 'zero' to 'nine'.
    """
    num_list = [int(num) for num in input_str.split()]
    sorted_num_list = sorted(num_list)
    return ' '.join(map(str, sorted_num_list))
```