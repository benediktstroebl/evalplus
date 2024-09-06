```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

Here's a step-by-step explanation of how the function works:
1. The function takes a string of numbers as input.
2. The input string is split into a list of individual numbers by the `split()` method. This method divides the string at each space and returns a list of the resulting string slices.
3. Then, a `List` comprehension is used to convert each element of the list to `int` and store them in the `numbers` list.
4. After that, the `sort()` method is applied to the `numbers` list to sort the numbers in ascending order.
5. Finally, the `map()` method is used to convert the sorted numbers back to a string, and ' '.join()' is used to concatenate the elements back into a single string with spaces in between. 

The function returns this sorted string.