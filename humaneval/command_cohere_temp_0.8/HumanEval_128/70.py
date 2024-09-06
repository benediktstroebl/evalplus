```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of each number in the array and stores them in the `signs` list. Subsequently, it returns the sum of the magnitudes multiplied by the product of all signs, accordingly. If the input array is empty, it returns `None`.

Here is a Markdown code block with inline comments to clarify the code:
```python
def prod_signs(arr):
    # Start by initializing the result to None. This is our default return value.
    result = None
    # If the input array is not empty, we proceed with the calculations.
    if arr:
        # Create two lists: 'magnitudes' to store the magnitude of each number, and 'signs' to store the signs of each number (1, -1, or 0).
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        # Calculate the final result as the sum of magnitudes multiplied by the product of signs.
        result = sum(magnitudes) * prod(signs)
    # If the input array is empty, we return None.
    return result
```
This script efficiently solves the problem and fulfills the requirements mentioned in the prompt. You can test it using the provided examples to ensure its functionality. Feel free to adapt this code to your needs or explore more problems if you're interested in further challenges!