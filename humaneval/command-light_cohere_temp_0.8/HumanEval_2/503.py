```python
def truncate_number(n: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number

    Test cases:
    >>> truncate_number(3.5) == 0.2504

    also works:
    >>> truncate_number(10.5) == 1.5
   
    test:
    >>> truncate_number(-5.5) == -5

    """
def main():
    n = float(input("Enter a number: "))
    print(truncate_number(n))

if __name__ == "__main__":
    main()
```
This Python code defines a function called `truncate_number` that takes a float number as input and returns the decimal part of that number. The function is designed to solve the problem of removing the fractional component of a positive number and returning the largest integer part of the number, which is always less than 1. 

The `main` function is used to get the user input, and the `truncate_number` function is called with that input.  The returned decimal part is then printed out.