```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the characters in the string to integers. The list function is used to convert the string to a list, and the upper method converts the string to uppercase to make the operation case insensitive.

Let's break down the solution into its components and explain how each part works:
1. **def digitSum(string)**: This line defines a function named digitSum that takes a single parameter string. This function is intended to calculate the sum of the ASCII values of the uppercase characters in the input string and return the result.
2. **return sum(map(int, list(string.upper())))**: This line contains the core logic of the solution and returns the output of the function. Let's break down this line further:
2.1. **sum(...)**: The sum function takes an iterable (in this case, a list) and returns the sum of all the elements in that iterable.
2.2. **map(int, ...)**: The map function takes two arguments: a function to apply to each item in the iterable, and the iterable itself. In this case, we are applying the int function to each character in the input string. The int function converts a string to its corresponding integer representation.
2.3. **list(...)**: The list function converts the string input into a list of characters. This is necessary because the map function requires an iterable, and we need to apply the int function to each character individually.
2.4. **string.upper()**: The upper method is called on the input string, which converts all the characters in the string to uppercase. This is done to ensure that the digit sum is calculated ignoring the case of the characters, making the solution case insensitive.

Putting it all together, the line returns the sum of the integer values of each character in the uppercased input string. This line effectively converts each character in the string to its ASCII value and then adds up all these values to provide the digit sum.

The solution is case-insensitive because of the .upper() method, and it can handle any string input, including empty strings, properly because of the list and int map operations.