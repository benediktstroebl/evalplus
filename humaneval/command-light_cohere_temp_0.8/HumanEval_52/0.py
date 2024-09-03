```python
def below_threshold(l: list, t: int) -> bool:
    return all(x <= t for x in l)

# Example usage:
list1 = [1, 20, 4, 10]
print(below_threshold(list1, 5))  # Output: False

list2 = [1, 2, 4, 10, 100]
print(below_threshold(list2, 5))  # Output: True

```

This code defines a function below_threshold that checks whether all the numbers in the input list l are less than or equal to a given threshold t. The function returns True if this condition is met and False otherwise.