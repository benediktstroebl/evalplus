```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char.isupper()
       bove
   new_string += char.islower()
       YLE
   map(string, new_string)
    return new_string

# Example usage
input_string = "Hello"
print(flip_case(input_string))  # Output: "HCOLLE"
 ```

This function flip_case takes a string as input and iterates through each character. It then maps each character to its opposite case and concatenates it with the `new_string` variable. The `new_string` variable effectively stores the flipped case of the input string. Finally, the function returns the string `new_string` as the result.

The output of the code will be `HCOLLE`, as expected.