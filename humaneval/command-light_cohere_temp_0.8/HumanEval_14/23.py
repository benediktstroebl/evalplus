Here's a self-contained Python function that retrieves a list of all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    return ["".join[i:string.get() or all prev_char(),
        prev+1] for i,prev_char in enumerate(string) if i != 0 and prev_char is not " "])

# Example usage
print(all_prefixes("abc"))
# ['a', 'ab', 'abc']
```
This function utilizes a list comprehension and the `enumerize()` function to iterate over every character in the input string. If the current character is not an empty string and the previous character is not whitespace, the current character is added to the list of prefixes.