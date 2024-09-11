### Median Calculator Script

Here is a Python script that implements a function to calculate the median of a list of numbers.

```markdown
### Code
```python
def median(l: list):
    """
    Return median of elements in the list l.

    :param l: A list of numbers.
    :return: The median of the numbers in the list.
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle value.
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle values.
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

### Explanation
This script uses Python's built-in `sorted` function to sort the list of numbers in ascending order. It then checks whether the length of the sorted list is odd or even.

- If the length is odd, the median is the middle value. This is because the list is sorted, so the middle value is the middle number.
- If the length is even, the median is the average of the two middle values. This is because the two middle values are equidistant from the median.

The script includes two test cases to demonstrate its functionality. The first test case uses a list with an odd length, and the second test case uses a list with an even length.