```python
def convert_numbers_to_words(arr):
    """
    Sort integers between 1 and 9, reverse, and replace with words.
    Ignore other numbers. Return empty array for empty input.

    Parameters:
        arr (list): A list of integers.

    Returns:
        list: Sorted, reversed, and replaced numbers as strings.
    """
    numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted([x for x in arr if 1 <= x <= 9])
    reversed_arr = sorted_arr[::-1]
    result = [numbers[x - 1] for x in reversed_arr]
    return result
```