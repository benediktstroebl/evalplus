Here is a self-contained Python script that defines the `below_threshold` function:
```python
def below_threshold(lst: list, t: int) -> bool:
    """Return True if all numbers in the list lst are below threshold t."""
    return all(num < t for num in lst)

# Test cases
if __name__ == "__main__":
    print(below_threshold([1, 2, 4, 10], 100))  # True
    print(below_threshold([1, 20, 4, 10], 5))   # False
```
This script defines the `below_threshold` function using the `all()` function with a generator expression. It then includes test cases to demonstrate the function's behavior.