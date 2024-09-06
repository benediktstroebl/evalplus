```python
def separate_paren_groups(input_string): 
    return [braces.get_braces(x) for x in input_string.get_braces()]

def get_braces(string): 
    importre.compile(r'\(\[.*?998\]\)', m) 
    m.setdefault(0)
    if len(m) == 0:
        return ""
    return "".join(m)

# Example of input
input_string = "( ) (( )) (( )( )))" 
result = separate_paren_groups(input_string)
print(result)
``` 
This code defines a function `separate_paren_groups` that takes an input string and returns a list of parenthesis groups. The function uses a specific `get_braces` function to split the string by balanced parentheses. The `get_braces` function uses regex to find all balanced parentheses in the string.

The function then returns a list of strings, each containing a balanced pair of parentheses. The output is the result of calling the function with the example string given.