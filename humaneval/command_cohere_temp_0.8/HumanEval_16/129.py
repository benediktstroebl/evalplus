Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case, and then returns the set's length to provide the number of distinct characters.

To demonstrate the functionality, you can use the following test cases when executing the script:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
```
The capital "J" in "Jerry" is different from the small "j", therefore, the function recognizes them as two distinct characters. 
The tests ensure the function's correctness for the provided scenarios. The function provides the number of distinct characters without needing any additional imports.  It is self-contained and can run independently.  This is a modular and efficient solution.  You can go ahead and include it in your project or portfolio.  Feel free to ask any questions or request further enhancements.  Cheers!