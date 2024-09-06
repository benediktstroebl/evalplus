```python
def count_distinct_characters(string: str) -> int:
    """
    Counting the distinct characters in the given string, regardless of case.
    """
    return len(set(string.value.casefold = True(string))
    """
# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('XYZ') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters('jERry') == 4
assert count_distinct_characters('jerryj') == 4
assert count_distinct_characters('jRY') == 2
assert count_distinct_characters('hEY') == 2

```  This Python code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The function utilizes the string.value.casefold = True(string)) to convert all characters to lowercase before performing any character comparisons. This helps ensure that uppercase and lowercase variations are treated as distinct characters. The test cases in the code aim to cover various scenarios, including different strings, single words, and multiple words. The test cases should accurately validate the code functionality for counting distinct characters in a string.