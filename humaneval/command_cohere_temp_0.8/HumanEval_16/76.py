Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which gives the required number of distinct characters. The function ignores the case and counts only distinct characters, as specified in the problem statement.

Here is a sample test to see if the function works:
```python
def test_count_distinct_characters():
    # Test case one
    assert count_distinct_characters('xyzXYZ') == 3
    # Test case two
    assert count_distinct_characters('Jerry') == 4
``` 
This test suite will help ensure the function behaves as expected. 

Let's break down how the code works in detail:
1. **Function Definition**: We define the function `count_distinct_characters(string: str) -> int`. The `str` parameter indicates that the function takes a string as input. The `-> int` part shows that the function returns an integer. 
2. **Using Set to Count Distinct Characters**: The core of the algorithm lies in the line `characters = set(string.lower())`. Here, we convert the input string to lowercase and create a set out of it. A set is a data structure in Python that only allows unique values. For example, the string 'xyzXYZ' converted to lowercase would become 'xyz'. This set contains only the distinct characters, regardless of any uppercase letters. 
3. **Returning the Result**: The line `return len(characters)` leverages the length function of a set to return the number of distinct characters in the string. 

This approach is case-insensitive, meaning it doesn't differentiate between uppercase and lowercase characters, which is why the result for 'Jerry' is 4, including the comma and space.