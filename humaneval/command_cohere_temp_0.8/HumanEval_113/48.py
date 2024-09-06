```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The Python script defines a function `odd_count` that takes a list of strings as input. It iterates through each string in the list and calculates the number of odd digits in each string. Then, it creates a list of Markdown strings indicating the count of odd elements in each string. The `enumerate` function is used to assign a unique index (starting from 1) to each string during the iteration, which is then embedded in the string to indicate which string the count refers to. The function returns this list of Markdown strings.

Here's an example usage and test case to ensure it matches the given specification:
```python
test_cases = [
    ['1234567', 'the number of odd elements in the string 1 of the input is 4'],
    ['3', 'the number of odd elements in the string 1 of the input is 1'],
    ['11111111', 'the number of odd elements in the string 1 of the input is 1'],
    ['12345678', 'the number of odd elements in the string 2 of the input is 1'],
    ['12345670', 'the number of odd elements in the string 3 of the input is 2'],
]

for test in test_cases:
    assert odd_count(test)[0] == test[1]
```