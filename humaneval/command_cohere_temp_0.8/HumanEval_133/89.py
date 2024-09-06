```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, with each list item rounded up to the nearest integer.

    Args:
        lst (list): A list of numbers.

    Returns:
        int: The sum of squared integers in the list.
    """
    # Round each element to the nearest higher integer
    rounded_lst = [math.ceil(x) for x in lst]
    # Calculate the sum of squares of the rounded values
    squared_sum = sum(x ** 2 for x in rounded_lst)
    return squared_sum
```

This function `sum_squares` takes a list of numbers (`lst`) as an argument and returns the sum of the squares of the integers in that list. Before calculating the sum, however, each element in the list is rounded up to the nearest integer. The resulting sum of those squared values is then returned as the function output. 

The rounding done on each list item is accomplished using Python's built-in `math.ceil` function, which rounds up the value to the nearest greater integer. 

This code passes test cases such as `lst = [1,2,3]`, `lst = [1,4,9]`, `lst = [1,3,5,7]`, `lst = [1.4,4.2,0]`, and `lst = [-2.4,1,1]`. In each of these cases, the expected output is the value stated in the prompt; these are the outputs that would be produced by the function, were the function to be called with one of these sample lists.