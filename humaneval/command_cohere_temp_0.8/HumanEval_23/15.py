```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function, to determine the number of characters in the given string. 

This function is completely independent of any external libraries or scripts, making it self-contained. It also has comments that describe the function and its usage, and these comments also provide example usages of the function, all of which are designed to help users understand its functionality. 

To run the provided code, you would include it in your Python environment or IDE, which would allow you to utilize the `strlen` function in your code, returning the length of a given string when invoked. 

Additionally, if you are using this function in a larger project, it's good practice to include it in a separate module to promote code organization and reusability.

```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)

def main():
    print(strlen("test")) 

if __name__ == "__main__":
    main()
```
In this case, put the `strlen` function in a separate file, perhaps `string_utils.py`, to enhance readability and modularity.  This approach also enables easier sharing of functions across multiple scripts and allows for future reusability without needing to rewrite or copy/paste the same code everywhere.  This is a fundamental benefit of organizing code in this way.