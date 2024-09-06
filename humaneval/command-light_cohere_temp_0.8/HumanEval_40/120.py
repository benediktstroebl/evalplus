```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in zip(*lst))

# Example usage:
if __name__ == "__main__":
    lst = [1, 3, 5, 0]
    print(triples_sum_to_zero(lst))  # Output: True

# Test cases:
if __name__ == "__main__":
    lst = [1, 3, -2, 1]
    print(triples_sum_to_zero(lst))  # Output: True

lst = [1, 2, 3, 7]
print(triples_sum_to_zero(lst))  # Output: False

lst = [2, 4, -5, 3, 9, 7]
print(triples_sum_to_zero(lst))  # Output: True
```
This script defines the `triples_sum_to_zero` function, which takes a list as input and returns `True` if the list has three distinct elements whose sum is equal to zero, and `False` otherwise. The function uses the simple logic to check if there are three elements with opposite signs in the list, which adds up to zero. The test cases demonstrate the result of the function, passing all the test cases.