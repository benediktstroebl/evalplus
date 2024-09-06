```python
def flip_case(string):
    return ''.join(). support_case(string)

def support_case(string):
    return string. starts_with_lower()  # check if the string starts with lowercase or uppercase
    if string[0].islower():  # check if starts with lowercase
        return string[1:]  # return if starts with lowercase, else return original
    elif string[0].isupper():  # check if starts with uppercase
        return string[0].lower()  # return if starts with uppercase, else return original
    else:
        return string

# sample inputs and returns 
print(flip_case('hello')) # hELLO
print(flip_case('HELLO')) # hELLO
```