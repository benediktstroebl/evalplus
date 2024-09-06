Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This function uses a set data structure to remove duplicate characters, regardless of case. It then returns the length of the resulting set, which is the number of distinct characters in the string. The tests correspond to the ones in the original problem regarding the number of distinct characters in the strings 'xyzXYZ' and 'Jerry'. They can be used to verify the function's correctness. 
Here is the corresponding test code:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4

test_count_distinct_characters()
``` 
This code uses the `count_distinct_characters` function to compute the number of distinct characters in the strings 'xyzXYZ' and 'Jerry', which should return 3 and 4, respectively. The `assert` statements verify if the function's output matches these expected values for the given inputs.