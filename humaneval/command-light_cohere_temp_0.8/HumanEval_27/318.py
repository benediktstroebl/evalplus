```python
def flip_case(string: str) -> str:
    new_str = ''.join(''.join(c, c[1:] if c[0].isupper() else(c[0].islower() else(c[1]) else c) for c in string)
    return new_str

# Example test cases
print(flip_case('Hello')) # 'hELLO'
print(flip_case('hello')) # 'HELLO'
print(flip_case('HELLo')) # 'hello'
print(flip_case('!@')) # '!bolder'
print(flip_case('A small sentence')) # 'sBoxuttEnE'
``` 
This function flip_case takes a string as input and iterates through each character. It then swaps the to uppercase if the original character is a lowercase and a lowercase if the original character is an uppercase. The function returns the string with the characters flipped.