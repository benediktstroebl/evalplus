### Median Calculator
#### Problem Solution

Here is a self-contained Python script that calculates the median of a given list of numbers.

```markdown
### Median Calculator

#### Problem Solution

A Python function that calculates the median of elements in a list.

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    :param l: A list of numbers
    :return: The median of the numbers in the list
    """
    return statistics.median(l)

# Example usage
if __name__ == "__main__":
    print(median([3, 1, 2, 4, 5]))  # Output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation

This script uses the built-in `statistics` module in Python to calculate the median. The `statistics.median()` function returns the median of a list of numbers.

This function takes a list of numbers as input and returns the median of the numbers in the list. The median is the middle value of the numbers in the list when the numbers are sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle numbers.

The example usage section demonstrates how to use the `median()` function with a list of numbers. The `if __name__ == "__main__":` block is used to ensure that the example usage code only runs when the script is run directly, not when it is imported as a module by another script.