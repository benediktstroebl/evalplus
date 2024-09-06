```python
def median(lst):
    # Sort the list
    sorted_numbers = sorted(lst)
    # Find the middle index
    middle = len(sorted_numbers)//2
    # Return the element at the middle
    return sorted_numbers[middle]

# Test cases
test_median = [
    [
        [-10, 4, 6, 1000, 10, 20],
        [5, 10, 6, 4, 3, 20],
        [-100, 2, 3, 101, 98],
        [0, 10, 0, 20, 30]
    ]

for test in test_median:
    actual_median = median(test)
    assert actual_median == (5 if len(test) % 2 == 0 else 10)
```