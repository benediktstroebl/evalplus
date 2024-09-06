```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
This Python script defines a function called `all_prefixes` that takes a single argument, `string`, which is of type `str`. This function returns a list, `List[str]`, of all the prefixes of the input string, arranged in ascending order from the shortest (comprising only the first character) to the longest (the entire input string).

Let's break down the operation of this function step by step:
1. **Initialization of the Prefixes List**: The function starts by creating an initial list named `prefixes`. This list starts with a single element, which is the first character of the input string. The first line of the function initializes `prefixes` as `[string[0]]`. The square bracket notation is used to index the string character by character. In Python, indexing starts from 0, so `string[0]` refers to the first character of the string.
2. **Appending Prefixes to the List**: The function then enters a loop to iterate over the characters of the input string, starting from the second character (index 1) down to the last character. Within this loop, the function appends to the `prefixes` list on each iteration. The appending is done using the `append` method of the list object, and it adds a new string to the end of the list. This new string is created by taking a slice of the input `string`, from the first character to the current character index (i.e., `string[:i]`). This effectively creates a new prefix with each iteration, and these prefixes are added to the list in the order they are created.
3. **Returning the Prefixes List**: Once the loop has finished iterating through all the characters, the function returns the `prefixes` list, which at this point contains all the prefixes of the input string in the desired order - from the shortest (the first character) to the longest (the entire string).

This function uses Python's powerful list capabilities and intuitive indexing to efficiently generate the desired prefixes and return them in the expected order.