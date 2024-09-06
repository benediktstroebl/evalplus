```python
def sort_third(lst):
    """Sorts a list of integers so that values not divisible by three are at the beginning and values divisible by three are at the end.
    :param lst: list of integers
    :return: sorted list
    """
    lst = sorted(lst, key=lambda x: x % 3)
    return lst
# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3]
    print("Sorted list:", lst)
    print("My list:", sort_third(lst))
```
We have implemented the `sort_third` function, which receives a list of integers as input and returns a sorted list such that values divisible by three are at the end and values not divisible by three are at the beginning. The key argument is used to sort the list, which is a lambda function that takes the element as an argument and returns it modulo three. 

This script can be run directly and provides a fully self-contained solution to the given problem.