Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case. It then calculates the length of this set to get the number of distinct characters. 

Here's a test case to verify the correct functionality of the function: 
```python
test_case = ['xyzXYZ', 'Jerry']
expected_result = [3, 4]

for i in range(len(test_case)):
    assert count_distinct_characters(test_case[i]) == expected_result[i], 'Test case failed!'
``` 
This test case provides a sense of how the function works and validates its correctness for the given input. 

Let me know if I've misunderstood the problem or if there's anything specific you'd like me to focus on in the solution. I'm here to help!