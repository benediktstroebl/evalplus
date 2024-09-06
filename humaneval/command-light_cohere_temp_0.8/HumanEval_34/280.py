```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in ['[]'] and x]

#Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ['a', 'b', 'c'],
    ['a', 'aa'],
    ['[][]', '[]'],
]

for test_case in test_cases:
    print(unique(test_case))
``` 
This function `unique` uses the Set data structure to quickly filter out duplicates and certain delimiters ('[]'). The output of each test case is then printed to the console.