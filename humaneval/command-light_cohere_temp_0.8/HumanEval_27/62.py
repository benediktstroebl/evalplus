```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():  #.: new_str += char.islower()
    provided:
            assert flip_case('Hello') == 'HELO', "Case 1: Failed"
            assert flip_case('hello') == 'olleH', "Case 2: Failed"
```  This function is designed to transform a given string, flipping the case of its characters. It achieves this goal by iterating through each character in the string.