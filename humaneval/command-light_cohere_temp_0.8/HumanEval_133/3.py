```python
def sum_squares(lst):
    """
    Compute the sum of squared numbers in the given list,
    round each element in the list to the upper integer(Ceiling) first.

    Args:
        lst (list) -> list of numbers

    Returns:
        int
    """
    return sum(map(lambda x: (x ** 2 + 1) ** .5, lst))

# Test cases
lst1 = [1,2,3]
assert sum_squares(lst1) == 14

lst2 = [1,4,9]
assert sum_squares(lst2) == 98

lst3 = [1,3,5,7]
assert sum_squares(lst3) == 84

lst4 = [1.4,4.0,1]
assert sum_squares(lst4) == 6

def main():
    print("Test cases passed!")
main()

# Call the main function
# For testing
```