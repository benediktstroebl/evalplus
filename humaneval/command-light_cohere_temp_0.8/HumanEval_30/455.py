```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
tests = [
    """Behaves as expected"""
    tests.add(get_positive([-1, 2, -4, 5, 6]))
    tests.add(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    tests.add(get_positive([2, -2, -3, 0, -1, 3, -3, 5, -5, 7]))

#Main execution
if __name__ == "__main__":
    print("Test Results:")
    for test in tests:
        print(test)
```