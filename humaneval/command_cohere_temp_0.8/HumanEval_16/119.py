Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which corresponds to the number of distinct characters. The function ignores the case, counting 'X' and 'x' as the same character. 

To apply this solution to test cases, one can simply call the function like this:
```python
test_cases = [
    'xyzXYZ', 
    'Jerry'
]

for test_string in test_cases:
    print(f'Test Case: {test_string} :: Output: {count_distinct_characters(test_string)}')
```
This will give the following output:
```
Test Case: xyzXYZ :: Output: 3
Test Case: Jerry :: Output: 4
```
The above code is a self-contained Python script that solves the problem using the function `count_distinct_characters`.