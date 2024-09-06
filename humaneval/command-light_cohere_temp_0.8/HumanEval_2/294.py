Here is a Python script that includes a self-contained function to truncate a given number: 

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    >>> return 0.5 if number <= 1 else
   
      round(number // 5)
    """ 
    return round(number // 5) if number > 1 else 0.5 

This code is an example of a self-contained function. It takes the language that defines a function and its use in one straightforward, clean, and efficient line. 

The function takes a number as input and returns the decimal part of the number, which is the fractional part after the decimal point has been removed. The function uses the number // 5 to round the number to a 5-digit integer before returning it as the decimal part.