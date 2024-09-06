Here's a self-contained Python function that returns unique elements from a list:
```python
def unique(lst):
    return list(set(lst))

# Test cases
tests = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [],
        [5, 2, 3, '123'],
        [123, 456, 789],
        ['a', 'a', 'bc'],
    ]
)

for test_case in tests:
    actual = unique(test_case)
    print(f"Test case: {actual}")
    print("\n")
```
This function utilizes the set difference method to achieve uniqueness and then converts the resulting set back into a list for the desired output. The test cases provided will also demonstrate the function's behavior for different inputs.