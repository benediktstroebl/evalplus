```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not:]

# Test cases
test_cases = [
    [list(range(10)),],
    ['text'],
    [123, '456', (1<<23) // 2],
    [1, 2, 3, 4, 5],
    [True, False, True]
]

for case in test_cases:
    assert unique(case) == case[1:]
``` 
This code defines a function unique that returns a list of unique elements from the input list lst. The function uses a set to keep track of the seen elements, and a list comprehension to filter out the duplicates. The test_cases list contains several test cases, each consisting of a list and the expected unique list as the output of the unique function. The code then iterates over each test case and compares the actual output with the expected unique list using the assert statement.