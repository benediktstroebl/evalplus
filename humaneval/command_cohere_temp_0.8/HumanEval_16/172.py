Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase to ensure that characters are treated as the same regardless of case and then adds them to the set. Finally, it returns the size of the set, which is the number of distinct characters. 

Here is how you can use this function in an interactive session to test it:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```
This function correctly counts the number of distinct characters in the input strings, as demonstrated by these test cases.  It handles cases like 'xyzXYZ' where there are duplicate characters and treats 'Jerry' as 'Jeri' with the same character set.  The set data structure ensures that duplicates are automatically counted only once.  Overall, the function provides a robust solution to the problem posed in the markdown code block.  If you have more questions or additional testing scenarios, feel free to ask.  This code can also be copied and pasted into a Python environment of your choice to use in your projects.