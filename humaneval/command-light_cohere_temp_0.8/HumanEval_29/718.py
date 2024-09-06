Certainly! Here is a self-contained Python script that implements the `filter_by_prefix` function to filter an input list of strings for ones that start with a given prefix: 
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    :param strings: list, all strings in it must start with the prefix
    :param prefix: string that must start the string
    :return: list, list of strings that start with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]

# test the function
test_strings = ['abc', 'bcd', 'cde', 'a', 'array', 'answer']
test_prefix = 'a'
test_result = filter_by_prefix(test_strings, test_prefix)
print(test_result)  # expected output ['abc', 'array']
```
This function takes two parameters: `strings`, which is a list of strings, and `prefix`, which is a string that must start the string in `strings`.  It returns a new list, containing all strings from `strings` that start with `prefix`.