```python
def median(l: list):
    """Return median of elements in the list l."""
    l.sort()
    median_numbers = sorted((n for n in l if n % 2 == 0))
    return (len(median_numbers) + 1) // 2 * sum(median_numbers)

def test_median():
    test_list = [10, 20, 1, 4]
    assert median(test_list) == 4.0

def test_list():
    return [1, 2, 4, 5]

test_median()
test_list()
```
The code defines a function `median` that calculates the median of the elements in a given list. This function first sorts thes the list, then selects the middle numbers (or the sum of middle numbers, depending on the length of the list) as the median. The function is then tested using a `test_median` function that creates a sample list and asserts the result of `median` with the correct value.