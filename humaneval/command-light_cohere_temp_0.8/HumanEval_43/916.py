```python
def pairs_sum_to_zero(l):
    """
    checks whether all elements in the list add up to zero.
    """
   
    list comprehension that will not work without list methods
    """
    return any(sum(x) <= 0 for x in l)
def test():
    """
    test suite function
    """
    test_list = [1, 3, 5, 0, -2, 1, 2, 3, 7]
    return not pairs_sum_to_zero(test_list)
if __name__ == "__main__":
    print("Testing function: ")
    print(test())
```
The code defines two functions: `pairs_sum_to_zero` checks whether the sum of all elements in a list is zero, using the `any()` function along with a list comprehension. The `test` function contains a list of numbers and uses the `pairs_sum_to_zero` function to check if all the numbers add up to zero. The `if __name__ == "__main__":` block ensures that the code is executed only when run as the script.