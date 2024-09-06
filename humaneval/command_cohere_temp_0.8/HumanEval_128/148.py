```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the input array and assigns them to the `magnitudes` list, it also calculates the signs of the integers in the input array and assigns them to the `signs` list. Subsequently, it calculates the sum of the magnitudes and the product of the signs, respectively, and returns their product as the result.

Here is a breakdown of the code:
- **Arrangement**: The code begins by testing if the input array is empty. If it's not empty, it proceeds to the next steps; otherwise, it returns immediately, which is an elegant way to handle a possible null input.
- **List Comprehension**: This is a concise way to create lists based on the contents of another list; in effect, you're creating two new lists (magnitudes and signs) from the original input array (`arr`) in one line of code.
- **Calculations**: The function calculates the sum of the magnitudes and the product of the signs in an efficient line of code each, utilizing Python's built-in functions for these operations.
- **Handling Results**: The function then returns the result of the computation, or None if the input array was empty.

This is a well-structured Python function that effectively utilizes built-in functions to solve the problem in a concise manner.