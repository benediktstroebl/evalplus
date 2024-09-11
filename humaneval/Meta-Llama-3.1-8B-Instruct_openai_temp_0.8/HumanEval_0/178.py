Here's a Python script that solves the problem:
```markdown
# Define a function to check if two numbers are close to each other
def are_close(num1: float, num2: float, threshold: float) -> bool:
    """
    Check if two numbers are within a certain threshold of each other.

    Args:
    num1 (float): The first number to compare.
    num2 (float): The second number to compare.
    threshold (float): The maximum difference between num1 and num2 to consider them close.

    Returns:
    bool: True if num1 and num2 are close, False otherwise.
    """
    return abs(num1 - num2) <= threshold


# Define the main function to check if any two numbers in a list are close
def has_close_elements(numbers: list[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (list[float]): The list of numbers to check.
    threshold (float): The maximum difference between two numbers to consider them close.

    Returns:
    bool: True if any two numbers in the list are close, False otherwise.
    """
    # Sort the numbers to make it easier to compare adjacent numbers
    numbers.sort()

    # Iterate over the sorted list of numbers, comparing each number with its adjacent numbers
    for i in range(1, len(numbers)):
        if are_close(numbers[i], numbers[i-1], threshold):
            return True

    # If we've reached this point, it means we haven't found any two close numbers
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a helper function `are_close` to check if two numbers are close to each other, and the main function `has_close_elements` to check if any two numbers in a list are close to each other. The main function sorts the list of numbers and then iterates over the sorted list, comparing each number with its adjacent number using the `are_close` function. If it finds any two close numbers, it returns `True`; otherwise, it returns `False`. The script also includes some test cases to demonstrate its usage.