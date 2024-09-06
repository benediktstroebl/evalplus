```python
def by_length(arr):
    unsort = sorted(arr)
    unsort.reverse()
    result = []
    for num in unsort:
        if 1 <= num <= 9: 
            result.append(str(num)[0] + "een")
    return result if result else []
```

The solution exploits the fact that the Python sorting algorithm returns the shortest number first. 

The test case for the code could be added to illustrate its usage:
```python
test = [
    ([2, 1, 1, 4, 5, 8, 2, 3], ['Eeen', 'Een', 'Een', 'Four', 'Five', 'Eight', 'Een', 'Three']),
    ([]      , []),
    (['a'], []),
    (555, ['Nine'])
]
for adata in test:
    assert by_length(adata[0]) == adata[1]
```

The test uses the `assert` statement which creates a ticket if the condition is not met, additionally, the output is printed out to visualize the resulting array.