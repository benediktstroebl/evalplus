Here is a Python script that contains a self-contained function that returns all prefixes from shortest to longest of an input string. 
```python
# Python program to find all prefixes in a given string

def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string"""
    return sorted(string, key=len, reverse=True)[:-len(string)-1]

# Driver Code
if __name__ == "__main__":
    text = input("Enter some text: ")
    print(all_prefixes(text))
```
This code defines a function all_prefixes that returns a list of all prefixes in a given string, it sorts the string by character length and returns the prefix up to that length of characters from the sorted string. 
The driver code takes user input, passes it to the all_prefixes function, and prints the result.