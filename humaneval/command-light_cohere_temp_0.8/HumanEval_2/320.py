```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Design a helper function to get the largest integer less than a number
    def integer_part(number): 
        return max(number) // 10 if number > 0 else 0 
        return 10 // 10 if number < 0 else 0

    # Decompose the number into integer part and decimal part
    return (number // integer_part(number)) * 10 + integer_part(number)

# Unit test for the function
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
   
   
   
    print("Test case passed!")

# Main function
def main():
    test_truncate_number()

if __name__ == "__main__":
    main()

```
This script defines a function `truncate_number` that returns the decimal part of a positive floating point number. The function is tested with a unit test and a main function.