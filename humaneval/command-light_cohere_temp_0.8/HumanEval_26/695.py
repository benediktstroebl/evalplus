Here's a self-contained Python function that solves the problem of removing duplicate integers from a list:
```python
def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique integers
    unique_numbers = set(numbers)

    # Convert the set back to a list
    return list(unique_numbers)

# Test cases
numbers1 = [1, 2, 3, 2, 4]
assert remove_duplicates(numbers1) == [1, 3, 4]

numbers2 = [3, 2, 4, 5, 6]
assert remove_duplicates(numbers2) == [3, 2, 4, 5, 6]

numbers3 = [1, 2, 3, 4, 5]
assert remove_duplicates(numbers3) == [1, 2, 3, 4]

numbers4 = [1, 2, 3, 5, 6, 7]
assert remove_duplicates(numbers4) == [1, 2, 3, 5, 6, 7]

numbers5 = [10, 20, 30, 10]
assert remove_duplicates(numbers5) == [10, 20, 30]
```
This Python code defines a function called `remove_duplicates` that takes a list of integers as input and removes duplicate elements from it. It uses the fact to create a set of unique integers and then converts it back to a list, effectively removing any duplicates. The code provides several test cases to validate the correctness of this function.