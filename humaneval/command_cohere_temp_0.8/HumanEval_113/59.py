```python
def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r
```

The above `odd_count` function iterates through the list of strings, summing up the number of odd digits in each string at a time, and then returning the count in the corresponding string as described in the problem.

Here is a test case to test the above function:
```python
test_cases = [
    ['1234567'], 
    ['3', '11111111'], 
    ['5', '55555557', '55555558', '55555000', '55555556'] 
]

expected_results = [
    ['the number of odd elements in the string 1 of the input is 4'], 
    ['the number of odd elements in the string 1 of the input is 1', 'the number of odd elements in the string 8 of the input is 8']
]

for i in range(len(test_cases)):
    assert odd_count(test_cases[i]) == expected_results[i]
```