```python
def strlen(string: str) -> int:
    return len(string)

# Test the function with different inputs
assertEqual(strlen(''),      0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('hello world!')), 11

#Example of using the function
print(strlen('hello world!'))
 ```