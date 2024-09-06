```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():
            new_str += char.islower()
    oleh
       
    if char.isupper():
            new_str += char.isupper()
    dry
``` 
The function flip_case takes a string and iterates through each character. It then converts characters that are currently in uppercase to lowercase and vice versa. The output is a new string that retains the original case of characters but interchanges the case of the characters.