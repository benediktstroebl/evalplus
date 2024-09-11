### below_threshold Function

The following Python script defines the `below_threshold` function, which checks if all numbers in a given list are below a specified threshold.

```markdown
### below_threshold Function

```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of numbers
        threshold (int): The threshold value
        
    Returns:
        bool: True if all numbers are below threshold, False otherwise
    """
    return all(num < threshold for num in numbers)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

### Explanation

-   The function `below_threshold` takes two parameters: `numbers` (a list of numbers) and `threshold` (an integer value).
-   It uses the built-in `all` function along with a generator expression to check if all numbers in the list are below the threshold.
-   The `all` function returns True if all elements of the iterable (in this case, the generator expression) are true. If at least one element is false, it returns False.
-   In the example usage section, we demonstrate the function's behavior with the provided test cases.