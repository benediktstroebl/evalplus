```python
def flip_case(string: str) -> str:
    new_string = ''.join()
    for c in string:
        if c.islower():  #
            new_string = c.titlecase()
         # Add to new_string and continue
        else:
            new_string = c.tolower() + ''.titlecase()
    return new_string
 ```