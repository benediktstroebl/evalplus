```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """
    string_sequence(0)
    '0'
    """
    return f"0 {n} {n+1} {n+2}"  # generating string usingformatted string and formatting params

if __name__ == "__main__":
    n = int(input("Enter the number to generate the sequence: "))
    print(string_sequence(n))
```