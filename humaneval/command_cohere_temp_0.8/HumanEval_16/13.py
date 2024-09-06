Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to store the unique characters in the string, regardless of case, and returns the count of distinct characters. Test cases are not included in the code but can be added to validate the functionality of the script. 
**NOTE:** The code uses the `lower()` method to convert the characters in the string to lowercase for consistent comparison, as per the prompt's instructions to ignore case distinctions. 

Let's break down the code step by step:
1. **Function Definition**: 
   ```python
   def count_distinct_characters(string: str) -> int:
   ```
   Here, we're defining a function named `count_distinct_characters` that takes a single argument called `string` (with a type hint of `str`), and returns an integer.
2. **Creating a Set of Unique Characters**:
   ```python
   characters = set(string.lower())
   ```
   In this line, we're creating a set called `characters` by converting the input `string` to lowercase using the `lower()` method. Storing the characters in a set ensures that only unique characters remain (case-insensitive) whereas repeated or redundant characters get automatically filtered out. 

3. **Returning the Distinct Character Count**:
   ```python
   return len(characters)
   ```
   This line returns the length of the `characters` set, which is directly proportional to the number of distinct characters in the input string. 

The function thereby effectively solves the problem and returns the number of distinct characters in the input string. 

Remember, this code is deterministic and will give the same results for the same input, and is resilient to grammatical variations or case differences. 

You can use it in a Markdown cell as:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```
This will generate the exact same docstring and test cases as provided in the problem statement.