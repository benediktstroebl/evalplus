```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the string, generating prefixes of increasing length
    for i in range(1, len(string) + 1):
        # Append the current prefix to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Example usage:
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    prefixes = all_prefixes(input_string)
    print("All prefixes of '{}' are:".format(input_string))
    for prefix in prefixes:
        print(prefix)
```