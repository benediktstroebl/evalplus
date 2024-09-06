```python
def count_distinct_characters(string: str) -> int:
    return len(string.isupper()) - 
print("Result:", count_distinct_characters('XYZ'))
print("Result:", count_distinct_characters('jerry'))

```
This function computes the number of distinct characters in a given string, regardless of case. It achieves this by checking if each character in the string is uppercase using the `isupper()` method. The function then returns the expected number of distinct characters in the string. 

You can use this function to test it with different inputs and see the result.