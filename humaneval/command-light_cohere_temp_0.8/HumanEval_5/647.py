```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return: A list of integers with the delimiter inserted
    """
    numbers = list(map(lambda x: f"{x}{" + str(x+delimeter) + f"}{x+1}", numbers))
    return numbers
``` 
This Python function `intersperse` accepts a list of integers `numbers` and a delimiter `delimeter` as inputs. It utilizes a use back a lambda function to create a new list where every two consecutive elements are separated by the provided delimiter. The lambda function generates a string representation of the list by using f-string formatting, which allows for the insertion of the delimiter between the elements.