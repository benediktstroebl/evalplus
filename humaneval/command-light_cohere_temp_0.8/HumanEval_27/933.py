```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():
            new_str += char.islower()
        if char.islupper()
        might.lower()
        for char in string:
        new_str += char.isupper()
       } else:
            new_str += char.islower()
``` 
# Example test cases 

print(flip_case('Hello'))  # Output: 'H€LLO'
print(flip_case('HELLO'))  # Output: 'hello'
print(flip_case('hELLO'))  # Output: 'H@LLO'
print(flip_case('HELLÃ'))  # Output: 'hella'
print(flip_case('!!HÃLLO'))  # Output: '!!hl@lo'
```