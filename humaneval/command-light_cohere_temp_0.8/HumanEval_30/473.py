```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test cases
test_get_positive = [
    dict(zip(['get_positive'], [
        [-1, 2, -4, 5, 6],
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    ]))
]

# Run the function and check the results
for case in test_get_positive:
    assert get_positive(case['get_positive']) == case['expected'],
    print(f"Case {case['name']} passed.")
```
The function takes a list lst as input and returns a new list containing only the positive numbers from the original list. This is process iterates through each element in the list through the > 0 condition and adds it to the new list.