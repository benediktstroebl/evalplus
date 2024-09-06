```python
def median(l: list):
    """Return median of elements in the list l."""
    return (sum(sorted((x for x in l if x <= len(l) / 2)))) / 2.0
``` 
This Python function calculates the median of a given list of numbers. The function sorts the numbers and returns the median as the average of the two middle numbers.