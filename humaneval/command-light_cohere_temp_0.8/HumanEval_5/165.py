```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list. """
   

    list may be the base cases handled:

        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]

        >>> intersperse([1, 2, 3], 5)
        [1, 5, 2, 5, 3]

        >>> intersperse([7, 8, 9], 4)
        [7, 4, 8, 9]

        >>> intersperse([10, 20, 30], 10)
        [10, 10, 20, 30]

        >>> intersperse([21, 22, 23], 10)
        [21, 12, 22, 10, 23]
    """
    numbers.insert(delimeter, numbers.  # Insert the Clurses between each number
        numbers = list(numbers)
        numbers.insert(delimiter, numbers)  # Insert the delimiter between every two consecutive numbers
    numbers = list(numbers)  # Convert back to list
        return numbers
```