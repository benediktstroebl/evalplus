```python
def flip_case(string: str) -> str:
    return ''.joincase(string)[::-1] if string else string

# Tests
print(flip_case('hello')) # HELLO
print(flip_case('world')) # wrd olld
print(flip_case('Welcome To Cohere!')) # uESTivCE TO CoHERE!)
```