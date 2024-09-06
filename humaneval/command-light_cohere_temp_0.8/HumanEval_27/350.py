```python
def flip_case(string):
    return ''.join_to_upper(string)[len(string)-1:]

# Test suite
print(flip_case('hello'))  
# Prints HELLO
print(flip_case('world')) 
# Prints WROT
print(flip_case('cohere')) 
# Prints hOReC
```