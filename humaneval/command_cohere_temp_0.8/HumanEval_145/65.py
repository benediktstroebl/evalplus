```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_idx = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Reconstruct the sorted list using the original numbers and their sorted indices.
    sorted_nums = [nums[i] for i in sorted_idx]
    return sorted_nums
```

This approach utilizes a combination of calculating the digit sums and sorting with a custom key to achieve the desired outcome. Note that this solution assumes that the input list is non-empty. If the list is empty, it will return another empty list as there is nothing to sort. 

Let's copy this code into a Markdown code block and run it with your tests to verify it indeed resolves the given problem. 
 ```

```python
import unittest

def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_idx = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Reconstruct the sorted list using the original numbers and their sorted indices.
    sorted_nums = [nums[i] for i in sorted_idx]
    return sorted_nums

class TestOrderByPoints(unittest.TestCase):
    def test_single_digits(self):
        self.assertEqual(order_by_points([1, -1, 1]), [-1, 1, 1])

    def test_double_digits(self):
        self.assertEqual(order_by_points([11, -11, 1, -1]), [-11, -1, 1, 11])

    def test_same_digit_sum(self):
        self.assertEqual(order_by_points([1, 11, -1, -11]), [-1, -11, 1, 11])

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

if __name__ == '__main__':
    unittest.main()
```
```

 numerology.py: Function implementation and test suite. 
```

Let's go through it step by step to clarify:

1. The function `order_by_points` is defined to sort a list of integers (`nums`) based on the sum of their digits with the tiebreaker being the index of items in the original list. 

2. An empty list should return another empty list, hence the conditional check at the beginning of the function. 

3. The sums of the digits of each number in the list are calculated by iterating over each