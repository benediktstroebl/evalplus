```python
def sort_third(lst):
    """This function sorts a list such that numbers not divisible by three maintain their relative order while numbers divisible by three are sorted consistently.
    
    Args:
        lst (list): list of numbers
    Returns:
        list: sorted list of numbers
    """
    return sorted(lst, key=lambda x: not_is_divisible(x, 3))

def not_is_divisible(x, divisor):
    """Determine whether a number is divisible by a divisor."""
    return divisor == 0 or x % divisor == 0

# Test the function
# Example usage
lst = [5, 6, 3, 4, 8, 9, 2]
sorted_lst = sort_third(lst)
print("Sorted list:", sorted_lst)
```
This function takes a list of numbers and returns a sorted list of numbers, where the numbers that are not divisible by three will maintain their relative order, and the numbers that are divisible by three will be sorted consistently. The function uses the specific logic to determine whether a number is divisible by three, and returns a sorted list of numbers accordingly.