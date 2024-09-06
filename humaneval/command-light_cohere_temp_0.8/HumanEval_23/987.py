Here is a self-contained Python function that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)
```

This function takes a string `string` as input and returns an integer representing its length. It uses the quite straightforwardly uses the string's `len` method to get its length.

Let's break down the code even further:
- The function `strlen` is defined with a single parameter `string: str`.
- The return type of the function is specified as `int`, which is an integer data type.
- Inside function simply calls the string's `len` method using the parameter string. This method returns an length of the string in terms of the number of characters it contains, and that's precisely what the function returns.
- In the example provided, the function is then called with the string '' (two underscores) and the length of the resulting string is returned and assigned to the variable `result`.

This function is self-contained, and it can be used to calculate the length of any given string. The function follows the standard Python style and is easy to read and understand.

Let's try using the function with some examples:
- If you call the `strlen` function with an empty string `''` (two underscores), the returned value will be 0.
- If calling the `strlen('abc')`, you'll get the length of the string 'abc' which is 3. The string 'abc' has 3 characters, which is why we get a length of 3.

This function can be used for various string calculations and is a good example of a self-contained Python function.