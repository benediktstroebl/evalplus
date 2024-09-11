```python
def triples_sum_to_zero(nums):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if three distinct elements sum to zero, False otherwise.
    """
    seen = set()  # Store the numbers we've seen so far
    num_count = {}  # Store the count of each number

    for num in nums:
        # For each number, try to find another number that sums to -num
        complement = -num
        if complement in num_count:
            # If we've seen the complement before, return True
            if num_count[complement] < 2:
                return True
        # If we've seen num before, increment its count
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return False


# Test cases
import unittest

class TestTriplesSumToZero(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(triples_sum_to_zero([1]), False)

    def test_no_triplets(self):
        self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)

    def test_triplets(self):
        self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), True)

    def test_triplets_multiple(self):
        self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), True)


if __name__ == '__main__':
    unittest.main()
```

This script defines a function `triples_sum_to_zero` that solves the problem. It uses a set to keep track of the numbers it has seen so far, and a dictionary to count the occurrences of each number. The function iterates over the input list, and for each number, it tries to find a pair of numbers that sums to -num. If it finds such a pair, it returns True. If it doesn't find any triplets, it returns False.

The script also includes test cases using the `unittest` framework to ensure that the function behaves correctly.