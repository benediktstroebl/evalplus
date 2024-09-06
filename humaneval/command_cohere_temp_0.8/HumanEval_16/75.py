Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to remove duplicate characters and converts the input string to lowercase to ensure that uppercase and lowercase characters are treated the same. It then returns the length of the set, which is the number of distinct characters. 

Here's a usage example to explain the behavior of the function:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
>>> count_distinct_characters('a' * 100)
1
```
In the examples, the function first handles the case where distinct characters 'x', 'y', 'Z', and 'X' are present in the string, returning 3. It then handles the case where distinct characters 'J', 'e', 'r', and 'y' are present in the string, returning 4. Finally, it proves that the function correctly handles duplicate characters in a string by returning 1 for the argument `'a' * 100`, which contains 100 identical characters.  By providing these examples, the code demonstrates the expected behavior of the function and validates its correctness.  Overall, the provided code showcases the solution to the problem in a clear and effective manner.