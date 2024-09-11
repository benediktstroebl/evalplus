```python
import statistics
import random

def test_median():
    # Test case 1: middle value is exact
    assert median([3, 1, 2, 4, 5]) == 3
    
    # Test case 2: middle value is average
    input_list = [-10, 4, 6, 1000, 10, 20]
    other_input_list = [-10, 4, 6, 1000, 20]
    assert round(median(input_list), 1) == 15.0
    # Randomly sorting the list to test the case when the list is sorted randomly
    random.shuffle(other_input_list)
    assert round(median(other_input_list), 1) == 15.0

def median(l: list):
    """Return median of elements in the list l."""
    return statistics.median(l)

if __name__ == "__main__":
    test_median()
```

This Python script includes the `statistics.median(l)` function from the Python standard library to calculate the median of a list. The `test_median()` function tests the `median()` function with two cases: one with an exact middle value and another with an average middle value. If both test cases pass, the script will run without any errors. 

However, if you want to implement the median calculation manually, you could replace the `median(l)` function with the following code:

```python
import statistics

def test_median():
    # Test case 1: middle value is exact
    assert median([3, 1, 2, 4, 5]) == 3
    
    # Test case 2: middle value is average
    input_list = [-10, 4, 6, 1000, 10, 20]
    other_input_list = [-10, 4, 6, 1000, 20]
    assert round(median(input_list), 1) == 15.0
    # Randomly sorting the list to test the case when the list is sorted randomly
    random.shuffle(other_input_list)
    assert round(median(other_input_list), 1) == 15.0

def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 0:
        # If the list has an even number of elements, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element
        return sorted_l[n // 2]

if __name__ == "__main__":
    test_median()
```