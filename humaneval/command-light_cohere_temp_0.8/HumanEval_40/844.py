```python
def triples_sum_to_zero(l):
    """
    Checks if all triple sums in list to zero.
    Returns: True if there are three distinct elements in the list that sum to zero,
    and False otherwise.
    """
    def test_passes_sum_to_zero(lst):
        return all(sum(x) == 0 for x in l)
    return test_passes_sum_to_zero(l)

# Example usage:
if __name__ == "__main__":
    lst = [1, 3, 5, 0]
    print(triples_sum_to_zero(lst))  # Output: True

test_sum_to_zero.test()  # A list of integers [1, 3, -2, 1]
test_sum_to_zero.test()  # The list [1, 2, 3, 7]
test_sum_to_zero.test()  # A list of integers [2, 4, -5, 3, 9, 7]
test_sum_to_zero.test()  # An empty list
```